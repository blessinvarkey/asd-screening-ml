import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt
import missingno
import seaborn as sns
import unittest

class ASDScreening:

#constructor
    def __init__(self):
        self.data = []

    def read_file(self, dataset):
        with open(dataset, 'r') as file:
            print(pd.read_csv(file))
            self.data = df

    def oneHotEncoding():
        pass

    def train_test_split(self, df, train_frac = 0.7, seed=1):
        df_matrix = df.values
        np.random.seed(seed)
        np.random.shuffle(df_matrix) #shuffle the data
        train_size = int(df_matrix.shape[0]*train_frac) #train the data
        train_features = def_matrix[:train_size, :-1] #except last column
        train_labels = df_matrix[:train_size, -1] #last column
        test_features = df_matrix[train_size:, :-1] #test data
        test_labels = df_matrix[train_size:, -1]

        return (train_features, train_labels), (test_features, test_labels)

    def plot_heatmap(self):
        fig = plt.figure(figsize=(12,10))
        sns.heatmap(self.data.corr())

dataset_adult = ASDScreening()
dataset_adult.read_file("Autism_Data.arff")



#Unit test
# class TestASDScreening(unittest.TestCase):
#     assert read_file(df = "Autism_Data.arff") == True
