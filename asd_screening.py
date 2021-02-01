
import numpy as np
import pandas as pd
import missingno

#Model
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, roc_auc_score, roc_curve, classification_report
from sklearn.preprocessing import LabelEncoder

"""""""""Load the Dataset"""""""""

df_adult = pd.read_csv("Autism_Data.arff")
df_adult = df_adult.replace('?', np.nan)
#print(df_adult.head(5))
#print(df_adult.columns)
df_adult = df_adult.rename(columns = {'A1_Score':'A1', 'A2_Score':'A2', 'A3_Score':'A3', 'A4_Score':'A4', 'A5_Score':'A5', 'A6_Score':'A6','A7_Score':'A7', 'A8_Score':'A8', 'A9_Score':'A9', 'A10_Score':'A10', "jundice":"jaundice", "austim":"autism", "contry_of_res": "country","Class/ASD": "Class_ASD" })
#print(df_adult.columns)
df_adult.drop(['country', 'ethnicity', 'used_app_before' , 'age','age_desc','relation', 'result'],axis=1, inplace=True)
#print(df_adult.columns)
#print(df_adult.dtypes)

"""""""""One Hot Encoding"""""""""

le = LabelEncoder()
df_adult.gender = le.fit_transform(df_adult.gender)
df_adult.jaundice = le.fit_transform(df_adult.jaundice)
df_adult.autism = le.fit_transform(df_adult.autism)
df_adult.Class_ASD = le.fit_transform(df_adult.Class_ASD)
#print(df_adult.dtypes)


""""""""""train_test_split"""""""""
def train_test_split(df_adult, train_frac=0.7, seed=1):
    df_matrix = df_adult.values

    #shuffle the dataset
    np.random.seed(seed)
    np.random.shuffle(df_matrix)

    #train_features
    #train_labels
