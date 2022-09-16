import pandas as pd
import os
import csv
import glob

input_path = '/aul/homes/qli027/projects/disaggregation/final_version/data/realdata/original_data/'
output_path = '/aul/homes/qli027/projects/disaggregation/final_version/data/realdata/1h/'


for name in glob.glob(input_path + '*.csv'):
    file_name = name.split('/')[-1]
    df = pd.read_csv(name,index_col=[0])
    df['Time'] = pd.to_datetime(df['Time'], format='%Y-%m-%d  %H:%M:%S')
    df.index = df['Time'] #change time to index
    df = df.drop('Time', axis=1)#change time to index
    df = df.resample('1h').sum()
    df.to_csv(output_path + file_name, header=True)
    

