import pandas as pd
import numpy as np
import os
import csv
from sklearn.metrics import matthews_corrcoef
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from math import sqrt
from sklearn.metrics import accuracy_score
from sklearn.metrics import f1_score
metric = {}
met = 'MCC'
# for house_num in range(14,16):
# devices = [4322480268,3424383659,1130799754,921227642,684659082]
# devices = [534856478,89811281]
devices = [4322480268.0,684659082.0]
sum = 0
ratio = {}
for device in devices:
    sum = sum + device 
print(sum)
for i in range(0,2):
    ratio[i] = devices[i]/sum
print(ratio)    
# threshold  = 20000    
models = ['FHMM']
# models= ["CO",'RNN','WindowGRU','DAE','Seq2Seq','Mean','FHMM'
Sum = {} 
periods = ['1min','3min','5min','10min','30min','1h']
for period in periods :
    input_path =  '/aul/homes/qli027/projects/disaggregation/final_version/prepare_for_figures/noise/VPN/prediction/' + str(period) + '/' 
    output_path = '/aul/homes/qli027/projects/disaggregation/final_version/prepare_for_figures/noise/VPN/prediction/' +str(period) + '/' + 'mcc.csv'

    for threshold in range(0,50000,1000):
    # threshold = 2000
        for model in models:
            sum_ = 0
            # for i in [2,3,4,5,6]:
            for i in [6]:

                groundtruth = pd.read_csv(input_path + 'groundtruth.csv')
                prediction = pd.read_csv(input_path +  str(model) + '.csv')

            #         header_device.append(i)
                gt_ = np.array(groundtruth.iloc[:,[i]])
                gt_ = np.where(gt_<= threshold,0,1)
                pred_ = np.array(prediction.iloc[:,[i]])
                pred_ = np.where(pred_<= threshold,0,1)
                Sum[i] = matthews_corrcoef(gt_,pred_)
            with open(output_path , 'a') as f:
                writer = csv.writer(f)
                writer.writerow([threshold,Sum[6]])    
