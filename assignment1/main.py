import sys
sys.path.append('.')
from data_preprocess import *
from train_spacy import *
from evaluate_func import *

if __name__ == '__main__':
    ##split lines by \n
    # data('./data/mod_tain.csv', 'train_new', './data/train')
    # data('./data/test.csv', 'test_new', './data/test')
    # train_spacy_model_('./data/train_new_spacy.json', './data/test_new_spacy.json', './models/split_lines_main')
    # model_eval('./models/split_lines_main', './data/test_new_spacy.json')
    model_eval('./models/split_lines_main', './data/train_new_spacy.json')

    # split lines with fixed len 500 characters
    # data('./data/mod_tain.csv', 'train_fixedlen', './data/train')
    # data('./data/test.csv', 'test_fixedlen', './data/test')
    # train_spacy_model_('./data/train_fixedlen_spacy.json', './data/test_fixedlen_spacy.json', './models/split_fixedlen_main')
    # model_eval('./models/split_fixedlen_main', './data/test_fixedlen_spacy.json')
    # model_eval('./models/split_fixedlen_main', './data/train_fixedlen_spacy.json')