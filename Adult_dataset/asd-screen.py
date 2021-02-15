import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt
import missingno
import seaborn as sns
import unittest

class ASDScreening():

#def read_file(self, file_name, sample=True):
with open("Autism_Data.arff", 'r') as file:
    df = pd.read_csv(file)
    print(df)
