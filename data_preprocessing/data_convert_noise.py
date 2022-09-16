

import pandas as pd
import numpy as np
import os

# input_path = '/aul/homes/qli027/projects/disaggregation/data/N_houses/sample_data/'
# output_path = '/aul/homes/qli027/projects/disaggregation/final_version/data/N_houses/' 
input_path = '/aul/homes/qli027/projects/disaggregation/final_version/data/N_houses_sample_with_noise/'
output_path = '/aul/homes/qli027/projects/disaggregation/final_version/data/N_houses_with_noise/' 

devices = ['noise','DropcamOut', 'LaptopOut', 'WelcomeOut', 'DayOut', 'MacBookOut', 'AmazonOut', 'TabOut', 'InsteonOut', 'sleepOut', 'SmartCamOut', 'BabyOut']

appliance_list = [3,5,6,7,8,9,10,13,16,18,20]


for i in range(4,12):
    
    path = os.path.join(output_path + str(i-1) + '/')
    os.mkdir(path)
    
    device_list = appliance_list[:i]
    
    for j in range(1,23):
        
        if j == 1:
            df = pd.read_csv(input_path  + str(i-1) + ".csv")

            columns = ['TIME']

            output_df = df.loc[:, columns]

            df['TIME'] = pd.to_datetime(df['TIME'],format='%Y-%m-%d %H:%M:%S')

            output_df['TIME'] = df['TIME'].values.astype(np.int64) // 10 ** 9            
            output_df['sum_'] = df['sum_']
            output_df.to_csv(path + 'channel_' + str(j) + '.dat',header=None,index=False,sep = ' ')
            
        elif j in device_list : 
            
            df = pd.read_csv(input_path  + str(i-1) + ".csv")

            columns = ['TIME']

            output_df = df.loc[:, columns]

            df['TIME'] = pd.to_datetime(df['TIME'],format='%Y-%m-%d %H:%M:%S')

            output_df['TIME'] = df['TIME'].values.astype(np.int64) // 10 ** 9
            
            device = devices[device_list.index(j)]
            
            output_df['sum'] = df[device]
            
            output_df.to_csv(path + 'channel_' + str(j) + '.dat',header=None,index=False,sep = ' ')
            
        else: 
            df = pd.read_csv(input_path  + str(i-1) + ".csv")

            columns = ['TIME']

            output_df = df.loc[:, columns]

            df['TIME'] = pd.to_datetime(df['TIME'],format='%Y-%m-%d %H:%M:%S')

            output_df['TIME'] = df['TIME'].values.astype(np.int64) // 10 ** 9            
            output_df['sum'] = df['sum']
            output_df['sum'].values[:] = 0 
            output_df.to_csv(path + 'channel_' + str(j) + '.dat',header=None,index=False,sep = ' ')                        




