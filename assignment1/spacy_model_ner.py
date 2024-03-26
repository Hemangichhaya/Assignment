import spacy
from spacy.training import Example, offsets_to_biluo_tags
from spacy.util import minibatch, compounding
import json, random
from spacy.scorer import Scorer
import sys
sys.path.append('.')
from data_preprocess import *


def extract_entity(model_location, filename, file_location):
  ner_model = spacy.load(model_location)
  lines = preprocess(filename, file_location)
  result = {}
  for line in lines:
    doc = ner_model(line)
    for ent in doc.ents:
      result[ent.label_] = ent.text
  return result