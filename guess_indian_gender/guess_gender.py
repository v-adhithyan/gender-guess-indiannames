import random
from collections import Counter
from pathlib import Path

import pandas as pd
from nltk import NaiveBayesClassifier
from nltk.classify import accuracy


class IndianGenderPredictor(object):

    def __init__(self):
        self.classifier = None
        self.test_set = None
        self.train_set = None

    def _gender_feature(self, n):
        n = str(n)
        return {
            'last_letter': n[-4:],
            'letter_counter': ((letter, count) for letter, count in Counter(n).items())
        }

    def _get_input_files(self):
        data_path = Path(__file__).parent / Path("data")

        return {
            'male': data_path / Path('Indian-Male-Names.csv'),
            'female': data_path / Path('Indian-Female-Names.csv')
        }

    def _get_data(self):
        labeled_data = {}
        for gender, file in self._get_input_files().items():
            df = pd.read_csv(file, dtype=str)
            labeled_data[gender] = df.name.values

        return labeled_data

    def _get_labelled_names(self):
        data = self._get_data()
        labeled_names = [(name, 'male') for name in data['male']]
        labeled_names.extend([(name, 'female') for name in data['female']])
        random.shuffle(labeled_names)

        return labeled_names

    def _split_train_test_data(self):
        featuresets = [(self._gender_feature(name), gender)
                       for name, gender in self._get_labelled_names()]
        train_length = int(len(featuresets) * 0.75)

        self.train_set = featuresets[0: train_length]
        self.test_set = featuresets[train_length:]

    def _get_classifier(self):
        self._split_train_test_data()
        self.classifier = NaiveBayesClassifier.train(self.train_set)
        return self.classifier

    @property
    def accuracy(self):
        """Returns accuracy of the classifier as float."""
        if not self.classifier:
            self.classifier = self._get_classifier()

        return accuracy(self.classifier, self.test_set)

    def predict(self, name):
        """
        Takes name as argument and returns gender.
        :param name: Indian gender name
        :return: male/female
        """
        if not self.classifier:
            self.classifier = self._get_classifier()

        return self.classifier.classify(self._gender_feature(name))
