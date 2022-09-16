import pandas as pd
import csv

input_path = '/aul/homes/qli027/projects/disaggregation/data/N_houses/1hour.csv'
output_path = '/aul/homes/qli027/projects/disaggregation/final_version/data/30_devices/device_sort.csv'
out_sort = '/aul/homes/qli027/projects/disaggregation/final_version/data/30_devices/sorted_device.csv'
df = pd.read_csv(input_path)
print(df.columns)

devices = ['AmazonIn', 'AmazonOut',
       'SwitchIn', 'SwitchOut', 'PrinterIn', 'PrinterOut', 'BabyIn', 'BabyOut',
       'MotionIn', 'MotionOut', 'scaleIn', 'scaleOut', 'LIFXIn', 'LIFXOut',
       'WeatherIn', 'WeatherOut', 'SpeakerIn', 'SpeakerOut', 'PlugIn',
       'PlugOut', 'iPhoneIn', 'iPhoneOut', 'AndroidIn', 'AndroidOut',
       'LaptopIn', 'LaptopOut', 'MacBookIn', 'MacBookOut', 'InsteonIn',
       'InsteonOut', 'DropcamIn', 'DropcamOut', 'SmartCamIn', 'SmartCamOut',
       'TabIn', 'TabOut', 'WelcomeIn', 'WelcomeOut', 'DayIn', 'DayOut',
       'ThingsIn', 'ThingsOut', 'SmokeIn', 'SmokeOut', 'BloodPressureIn',
       'BloodPressureOut', 'sleepIn', 'sleepOut', 'PhotoIn', 'PhotoOut']

# devices = [ 'AmazonTe_8a:73:76', 'Apple_52:a9:88', 'Apple_95:16:11', 'Azurewav_cf:ed:e3', 'BelkinIn_ff:91:1d', 'Chongqin_73:a8:57', 'Google_5c:72:62', 'Guangdon_a8:f0:5d', 'IntelCor_f3:d7:d9', 'LiteonTe_e2:cd:e5', 'Netgear_14:bf:e4', 'Netgear_14:bf:e6', 'Netgear_14:bf:e7', 'Netgear_bb:89:87', 'Nintendo_b3:3a:ce', 'PhilipsL_04:ae:96', 'Raspberr_8d:86:e1', 'Samjin_77:5f:d5', 'SichuanA_5f:b4:6d', 'Smarthom_45:73:31', 'Tp-LinkT_40:66:48']

with open(output_path, 'w', newline='') as outcsv:
    writer = csv.writer(outcsv)
    writer.writerow(["device", "sum", "ratio"])
outcsv.close()

Sum = df['TotalIn'].sum() +  df['TotalOut'].sum()

with open(output_path, 'a', newline='') as outcsv:
    writer = csv.writer(outcsv)
    writer.writerow(["total", Sum, 1])
outcsv.close()

for device in devices: 
    
    column_name = device
    column_sum = df[column_name].sum()
    ratio = '{0:.6f}'.format(column_sum/Sum)

    with open(output_path,  'a') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([column_name,column_sum,ratio])
    csvfile.close()
    
df = pd.read_csv(output_path)
df_ = df.sort_values(by=['sum'],ascending=False)
print(df_.device.tolist())
df_.to_csv(out_sort,index=False)
    


    

