import pandas as pd

import pandas as pd
import numpy as np

input_path = '/aul/homes/qli027/projects/disaggregation/final_version/prepare_for_figures/diff_granularity/data/VPN/'

output_path = '/aul/homes/qli027/projects/disaggregation/final_version/prepare_for_figures/noise/VPN/' 
sort_device = '/aul/homes/qli027/projects/disaggregation/final_version/prepare_for_figures/topk/VPN/sorted_device.csv'

df = pd.read_csv(input_path  + "1min.csv")

devices= ['Samjin_77:5f:d5', 'SichuanA_5f:b4:6d', 'Chongqin_73:a8:57', 'Smarthom_45:73:31', 'PhilipsL_04:ae:96', 'Nintendo_b3:3a:ce', 'IntelCor_f3:d7:d9', 'BelkinIn_ff:91:1d', 'Tp-LinkT_40:66:48', 'Azurewav_cf:ed:e3', 'Netgear_14:bf:e7', 'LiteonTe_e2:cd:e5', 'Guangdon_a8:f0:5d', 'Apple_95:16:11', 'Apple_52:a9:88', 'Raspberr_8d:86:e1']
# df_device = pd.read_csv(sort_device)
# devices= df_device['device'].tolist()

# print(devices)
    
columns = ['Netgear_14:bf:e6','Google_5c:72:62','AmazonTe_8a:73:76']

    
df1 = df.loc[:, columns]

df1['TIME'] = df['Time']
# df1['sum']= df['TotalOut']
df1['sum'] = df['Length'] - df['Netgear_bb:89:87'] - df['Netgear_14:bf:e4'] - df[devices].sum(axis=1)
df1['noise']  = df1['sum']  - df[columns].sum(axis=1)

# df1['sum']= df[columns].sum(axis=1)

df1.reset_index(drop=True, inplace=True)
# df1.to_csv(output_path + str(i)  + '.csv', header=True,index = False, mode='a+')
df1.to_csv(output_path + 'noise.csv', header=True,index = False, mode='a+')