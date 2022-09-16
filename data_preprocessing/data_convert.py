

import pandas as pd
import numpy as np
import os

input_path = '/aul/homes/qli027/projects/disaggregation/final_version/prepare_for_figures/topk/UNSW/'
output_path = '/aul/homes/qli027/projects/disaggregation/final_version/prepare_for_figures/topk/UNSW/' 


# devices = ['DropcamOut', 'AmazonIn', 'LaptopOut', 'DropcamIn', 'WelcomeOut', 'DayOut', 'MacBookOut', 'AndroidIn', 'AmazonOut', 'TabOut', 'InsteonIn', 'sleepIn', 'InsteonOut', 'sleepOut', 'SmartCamIn', 'WelcomeIn', 'SmartCamOut', 'BabyOut', 'BabyIn', 'ThingsOut', 'WeatherIn', 'ThingsIn', 'MotionOut', 'SpeakerOut', 'SpeakerIn', 'PhotoIn', 'MotionIn', 'AndroidOut', 'DayIn', 'LIFXIn', 'LIFXOut', 'PlugIn', 'iPhoneIn', 'PlugOut', 'PrinterOut', 'WeatherOut', 'PhotoOut', 'SwitchOut', 'iPhoneOut', 'PrinterIn']
# devices = [ 'WeatherIn', 'ThingsIn', 'MotionOut', 'SpeakerOut', 'SpeakerIn', 'PhotoIn', 'MotionIn', 'AndroidOut', 'DayIn', 'LIFXIn']
# devices = ['DropcamIn', 'LaptopIn', 'WelcomeIn', 'DayIn', 'MacBookIn', 'AmazonIn', 'TabIn', 'InsteonIn', 'sleepIn', 'SmartCamIn', 'BabyIn', 'ThingsIn', 'MotionIn', 'SpeakerIn', 'AndroidIn', 'LIFXIn', 'PlugIn', 'PrinterIn', 'WeatherIn', 'PhotoIn']
# devices = ['Netgear_bb:89:87', 'Netgear_14:bf:e6', 'Netgear_14:bf:e4', 'Google_5c:72:62', 'AmazonTe_8a:73:76', 'Samjin_77:5f:d5', 'SichuanA_5f:b4:6d', 'Chongqin_73:a8:57', 'Smarthom_45:73:31', 'PhilipsL_04:ae:96', 'Nintendo_b3:3a:ce', 'IntelCor_f3:d7:d9', 'BelkinIn_ff:91:1d', 'Tp-LinkT_40:66:48', 'Azurewav_cf:ed:e3', 'Netgear_14:bf:e7', 'LiteonTe_e2:cd:e5', 'Guangdon_a8:f0:5d', 'Apple_95:16:11', 'Apple_52:a9:88', 'Raspberr_8d:86:e1']

devices = ['DropcamOut', 'LaptopOut', 'WelcomeOut', 'DayOut', 'MacBookOut', 'AmazonOut', 'TabOut', 'InsteonOut', 'sleepOut', 'SmartCamOut']

# appliance_list = [3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22]
# appliance_list = [5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22]
appliance_list = [3,5,6,7,8,9,10,16,18,20]
for i in range(10,11):
    
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




