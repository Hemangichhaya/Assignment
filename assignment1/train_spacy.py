import spacy
from spacy.training import Example, offsets_to_biluo_tags, biluo_tags_to_offsets
from spacy.util import minibatch, compounding
import json, random

def train_spacy_model_(train_data_location, test_data_location, output_model_location):
  with open(train_data_location, 'r') as file:
    TRAIN_DATA = json.load(file)['data']

  with open(test_data_location, 'r') as file:
      TEST_DATA = json.load(file)['data']

  nlp = spacy.load('en_core_web_sm', disable=['tok2vec', 'tagger', 'parser'])
  ner = nlp.get_pipe("ner")
  for _, annotations in TRAIN_DATA:
    for ent in annotations.get("entities"):
        ner.add_label(ent[2])

  optimizer = nlp.resume_training()

  for itn in range(30):
    random.shuffle(TRAIN_DATA)
    losses = {}
    for batch in minibatch(TRAIN_DATA, size=compounding(4.0, 16.0, 1.001)):
        exm = []
        for text, annotations in batch:
            doc = nlp.make_doc(text)
            tags = offsets_to_biluo_tags(doc, annotations["entities"])
            entities = biluo_tags_to_offsets(doc, tags)
            ent = {}
            ent['entities'] = entities
            example = Example.from_dict(doc, ent)
            exm.append(example)
        nlp.update(exm, sgd=optimizer, drop=0.2, losses=losses)
        print(f'losses: {losses}')
  nlp.to_disk(output_model_location)
