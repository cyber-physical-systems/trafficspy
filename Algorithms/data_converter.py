

import pandas as pd
import numpy as np
import os

input_path = '/aul/homes/qli027/projects/disaggregation/final_version/prepare_for_figures/noise/VPN/'
output_path = '/aul/homes/qli027/projects/disaggregation/final_version/prepare_for_figures/noise/VPN/' 


# 'Samjin_77:5f:d5', 'SichuanA_5f:b4:6d', 'Chongqin_73:a8:57',
# devices = ['DropcamOut', 'LaptopOut', 'WelcomeOut', 'noise']
devices = ['Netgear_14:bf:e6','Google_5c:72:62','AmazonTe_8a:73:76', 'noise']

appliance_list = [5,6,7,8]

for i in range(4,5):
    
    path = os.path.join(output_path + str(i) + '/')
    os.mkdir(path)
    
    device_list = appliance_list[:i]
    
    for j in range(1,23):
        
        if j == 1:
            df = pd.read_csv(input_path  + str(i) + ".csv")

            columns = ['TIME']

            output_df = df.loc[:, columns]

            df['TIME'] = pd.to_datetime(df['TIME'],format='%Y-%m-%d %H:%M:%S')

            output_df['TIME'] = df['TIME'].values.astype(np.int64) // 10 ** 9            
            output_df['sum'] = df['sum']
            output_df.to_csv(path + 'channel_' + str(j) + '.dat',header=None,index=False,sep = ' ')
            
        elif j in device_list : 
            
            df = pd.read_csv(input_path  + str(i) + ".csv")

            columns = ['TIME']

            output_df = df.loc[:, columns]

            df['TIME'] = pd.to_datetime(df['TIME'],format='%Y-%m-%d %H:%M:%S')

            output_df['TIME'] = df['TIME'].values.astype(np.int64) // 10 ** 9
            
            device = devices[device_list.index(j)]
            
            output_df['sum'] = df[device]
            
            output_df.to_csv(path + 'channel_' + str(j) + '.dat',header=None,index=False,sep = ' ')
            
        else: 
            df = pd.read_csv(input_path  + str(i) + ".csv")

            columns = ['TIME']

            output_df = df.loc[:, columns]

            df['TIME'] = pd.to_datetime(df['TIME'],format='%Y-%m-%d %H:%M:%S')

            output_df['TIME'] = df['TIME'].values.astype(np.int64) // 10 ** 9            
            output_df['sum'] = df['sum']
            output_df['sum'].values[:] = 0 
            output_df.to_csv(path + 'channel_' + str(j) + '.dat',header=None,index=False,sep = ' ')                        




