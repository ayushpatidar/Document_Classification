import pandas as pd
import numpy as np
from scipy import stats
import argparse
import warnings


warnings.filterwarnings("ignore")

class load_data():

    def read_data(self, file_name):
        #if file is csv
        #df = pd.read_csv()

        #if file is json

        df = pd.read_json("Datasets/"+file_name, lines=True)

        #first 5 rows of dataframe are
        print(df.head())


        #columns of datframe are..
        print(df.columns)




parser = argparse.ArgumentParser(description="modelling")
parser.add_argument('--file_name', type=str, help="reading_file_name")
args = parser.parse_args()




object_load = load_data()

object_load.read_data(args.file_name)

