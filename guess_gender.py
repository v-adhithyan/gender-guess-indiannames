import random
from collections import Counter
from pathlib import Path

import pandas as pd
from nltk import NaiveBayesClassifier
from nltk.classify import accuracy

CLASSIFIER = None
TEST_SET = None


def _gender_feature(n) -> dict:
    n = str(n)
    return {
        'last_letter': n[-4:],
        'letter_counter': ((letter, count) for letter, count in Counter(n).items())
    }


def _get_input_files() -> dict:
    data_path = Path("data")

    return {
        'male': data_path / Path('Indian-Male-Names.csv'),
        'female': data_path / Path('Indian-Female-Names.csv')
    }


def _get_data() -> dict:
    labeled_data = {}
    for gender, file in _get_input_files().items():
        df = pd.read_csv(file, dtype=str)
        labeled_data[gender] = df.name.values

    return labeled_data


def _get_labelled_names() -> list:
    data = _get_data()
    labeled_names = [(name, 'male') for name in data['male']]
    labeled_names.extend([(name, 'female') for name in data['female']])
    random.shuffle(labeled_names)

    return labeled_names


def _get_classifier():
    featuresets = [(_gender_feature(name), gender)
                   for name, gender in _get_labelled_names()]
    train_length = int(len(featuresets) * 0.75)
    training_set = featuresets[0: train_length]
    test_set = featuresets[train_length:]
    classifier = NaiveBayesClassifier.train(training_set)
    # has an accuracy of 0.877
    return classifier, test_set


def get_accuracy():
    global CLASSIFIER, TEST_SET
    if not CLASSIFIER:
        CLASSIFIER, TEST_SET = _get_classifier()

    return accuracy(CLASSIFIER, TEST_SET)


def guess_gender(name):
    global CLASSIFIER, TEST_SET
    if not CLASSIFIER:
        CLASSIFIER, TEST_SET = _get_classifier()
    return CLASSIFIER.classify(_gender_feature(name))
