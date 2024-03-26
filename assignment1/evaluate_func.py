import spacy
from spacy.training import Example, offsets_to_biluo_tags, biluo_tags_to_offsets
from spacy.util import minibatch, compounding
import json, random
from spacy.scorer import Scorer

def evaluate(ner_model, examples):
    scorer = Scorer()
    ex = []
    for input_, annot in examples:
        doc = ner_model.make_doc(input_)
        tags = offsets_to_biluo_tags(doc, annot["entities"])
        entities = biluo_tags_to_offsets(doc, tags)
        ent = {}
        ent['entities'] = entities
        gold = Example.from_dict(doc, ent)
        gold.predicted = ner_model(str(gold.predicted))
        ex.append(gold)
    return scorer.score(ex)

def model_eval(model_location, test_data_location):
  ner_model = spacy.load(model_location)
  with open(test_data_location, 'r') as file:
      TEST_DATA = json.load(file)['data']

  results = evaluate(ner_model, TEST_DATA)
  print(results)
