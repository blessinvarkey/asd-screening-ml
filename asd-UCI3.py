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
            self.data = pd.read_csv(file)
#            print(self.data)
