import pandas as pd
import numpy as np
from scipy import stats

#if file is csv
#df = pd.read_csv()

#if file is json

df = pd.read_json("Datasets/News_Category_Dataset.json", lines=True)

#first 5 rows of dataframe are
print(df.head())


#columns of datframe are..
print(df.columns)