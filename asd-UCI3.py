import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt
import missingno
import seaborn as sns
#import unittest

class ASDScreening:

#constructor
    def __init__(self):
        self.data = []

    def read_file(self, dataset):
        with open(dataset, 'r') as file:
            self.data = pd.read_csv(file)
#            print(self.data)
    def missing_data(self):
        self.data = self.data.replace('?', np.nan)
#        print(self.data)
        self.missing_data = missingno.matrix(self.data, figsize =(30,10))
        plt.show()

    def columns(self):
        self.column = self.data.columns
        print(self.column)

    def spellcheck(self):
        self.data = self.data.rename(columns={})
        self.data.columns = ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9', 'A10','age', 'gender', 'ethnicity', 'jaundice', 'autism', 'country', 'used_app_before', 'result', 'age_desc', 'relation', 'ASD_label ']


    def plot_histogram(self):
        fig = plt.figure(figsize=(10,10))
        sns.countplot(y='country', data=self.data)
        self.data.country.value_counts()
        plt.show()

        fig = plt.figure(figsize=(10,6))
        sns.countplot(x="gender", data=self.data, facecolor=(0, 0, 0, 0), linewidth=5, edgecolor=sns.color_palette("dark", 3))
        plt.show()

        fig = plt.figure(figsize=(25,6))
        sns.countplot(y='jaundice', data=self.data);
        self.data.jaundice.value_counts()
        plt.show()

        fig = plt.figure(figsize=(25,6))
        sns.countplot(y='autism', data=self.data);
        self.data.autism.value_counts()
        plt.show()


    def data_types(self):
        self.dtypes = self.data.dtypes
        print(self.dtypes)

    def describe(self):
        self.describe = self.data.describe()
        print(self.describe)



    def nan_values(self):
        nAn = self.data.isnull().sum()
        print(nAn)

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
        plt.show()

def main():
    print("\n******* Adult Dataset *************\n")
    dataset_adult = ASDScreening()
    dataset_adult.read_file("Autism_Data.arff")
#    dataset_adult.missing_data()
    dataset_adult.columns()
    dataset_adult.spellcheck()
    dataset_adult.plot_histogram()
    dataset_adult.nan_values()
    dataset_adult.data_types()
    dataset_adult.describe()
    dataset_adult.plot_heatmap()

    print("\n******* Toddler Dataset *************\n")

#    dataset_toddler = ASDScreening()
#    dataset_toddler.read_file("Autism_Dataset.csv")
    # dataset_toddler.missing_data()
    # dataset_toddler.nan_values()
    # dataset_toddler.data_types()
    # dataset_toddler.describe()
#    dataset_toddler.columns()

if __name__ == '__main__':
    main()
