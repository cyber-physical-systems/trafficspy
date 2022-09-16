import pandas as pd

import pandas as pd
import numpy as np

input_path = '/aul/homes/qli027/projects/disaggregation/final_version/prepare_for_figures/diff_granularity/data/VPN/'

output_path = '/aul/homes/qli027/projects/disaggregation/final_version/prepare_for_figures/diff_granularity/data/VPN/' 
sort_device = '/aul/homes/qli027/projects/disaggregation/final_version/prepare_for_figures/topk/VPN/sorted_device.csv'

df = pd.read_csv(input_path  + "1min.csv")


df_device = pd.read_csv(sort_device)
devices= df_device['device'].tolist()

print(devices)
    
columns = []
for i in range(1,6):
    columns.append(devices[i])   
    print(columns)
    
df1 = df.loc[:, columns]

df1['TIME'] = df['Time']
# df1['sum']= df['TotalOut']
df1['sum'] = df['Length'] - df['Netgear_bb:89:87'] - df['Netgear_14:bf:e4']
# df1['sum']= df[columns].sum(axis=1)

df1.reset_index(drop=True, inplace=True)
# df1.to_csv(output_path + str(i)  + '.csv', header=True,index = False, mode='a+')
df1.to_csv(output_path + '5.csv', header=True,index = False, mode='a+')