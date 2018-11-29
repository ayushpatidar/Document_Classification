import warnings
import pandas as pd
import numpy as np
from scipy import stats
import nltk
from nltk.corpus import stopwords
import inflect


warnings.filterwarnings("ignore")

class cleaning():


    def tokenize(self, data_frame, column, n):
        """

        This function tokenize given column of a dataframe
        :param n: contain the n of n-grams technique
        :return:
        """
        data_frame[column] = data_frame[column].apply(lambda row: nltk.ngrams(row, n))



    def lower_case(self, data_frame, column):
        """
        This function convert given column into lower case..
        """
        data_frame[column] = data_frame[column].apply(lambda row: row.lower())



    def remove_stop_wprds(self, data_frame, column):
        """
        This function removes stopword from a given column

        """
        stop_words = set(stopwords.words("english"))

        data_frame[column] = data_frame[column].apply(lambda row: [item for item in row if item not in stop_words])


    def replace_number(self, data_frame, column):
        """
        This function convert number in numeric form into textual
        representation
        """

        convert = inflect.engine()

        data_frame[column] = data_frame[column].apply(lambda row:
                                                      [convert.number_to_words(word)
                                                       if word.isdigit() else word for word in row])
