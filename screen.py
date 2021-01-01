#Data Analysis
import math, time, random, datetime
import numpy as np
import pandas as pd

#Data visualisation
import matplotlib.pyplot as plt
import missingno
import seaborn as sns

#Machine Learning


df = pd.read_csv('Autism_Data.arff')
#Display first few rows
df.head(5)

# Display the last few rows
#df.tail(5)

#Identify missing values
missingno.matrix(df, figsize = (30,10))

#Fix the colunm names/spellings
df = df.rename(columns = {"jundice":"jaundice", "austim":"autism", "contry_of_res": "country", "Class/ASD":"asd_classification"})

df.isnull().sum()

df = df.replace('?', 0)
df['used_app_before'].value_counts()
df['relation'].value_counts()
df['A1_Score'].value_counts()
df['jundice'].value_counts()
df['ethnicity'].value_counts()
df['age_desc'].value_counts()
df['relation'].value_counts()
df['contry_of_res'].value_counts()
df.info()

new_df = pd.DataFrame({'gender': df.gender.map(dict(f=1, m=0))})
df.update(new_df)

pd.get_dummies(df['jaundice'])
