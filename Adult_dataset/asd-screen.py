import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt
import missingno
import seaborn as sns
import unittest

class ASDScreening():

    def read_file(self, file_name, sample=True):
    with open("Autism_Data.arff", 'r') as file:
        df = pd.read_csv(file)
        self.df = df


    def oneHotEncoding():
        pass

    def train_test_split(seld, df, train_frac = 0.7, seed=1):
        df_matrix = df.values
        np.random.seed(seed)
        np.random.shuffle(df_matrix) #shuffle the data
        train_size = int(df_matrix.shape[0]*train_frac) #train the data
        train_features = def_matrix[:train_size, :-1] #except last column
        train_labels = df_matrix[:train_size, -1] #last column
        test_features = df_matrix[train_size:, :-1] #test data
        test_labels = df_matrix[train_size:, -1]

        return (train_features, train_labels), (test_features, test_labels)



class TestASDScreening(unittest.TestCase):
   pass
