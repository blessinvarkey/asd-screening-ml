
import numpy as np
import pandas as pd

#Model
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, roc_auc_score, roc_curve, classification_report
from sklearn.preprocessing import LabelEncoder

#load the adult autism dataset
df_adult = pd.read_csv("Autism_Data.arff")
df_adult = df_adult.replace('?', np.nan)
print(df_adult.head(1))
df_adult = df_adult.rename(columns = {"A1_Score":"A1", "A2_Score":"A2", "A3_Score":"A3", "A4_Score":"A4", "A5_Score":"A5", "A6_Score":"A6", "A7_Score":"A7", "A8_Score":"A8", "A9_Score":"A9", "A10_Score":"A10", "jundice":"jaundice", "austim":"autism", "contry_of_res": "country"})
print(df_adult.columns)
