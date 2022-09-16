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
threshold = 970000
# for house_num in range(14,16):
# devices = [4322480268,3424383659,1130799754,921227642,684659082]
devices = [3424383659,921227642]
sum = 0
ratio = {}
for device in devices:
    sum = sum + device 
print(sum)
for i in range(0,2):
    ratio[i] = devices[i]/sum
print(ratio)    
    
# models = ['FHMM']
models= ["CO",'RNN','WindowGRU','DAE','Seq2Seq','Mean','FHMM']
input_path = '/aul/homes/qli027/projects/disaggregation/final_version/prepare_for_figures/different_approaches/data/VPN_/' 
output_path = '/aul/homes/qli027/projects/disaggregation/final_version/prepare_for_figures/different_approaches/data/VPN_/F1.csv' 
input_path_2 = '/aul/homes/qli027/projects/disaggregation/final_version/prepare_for_figures/different_approaches/data/VPN/' 


for model in models:
    sum_ = 0
    # for i in [2,3,4,5,6]:
    for i in [3,5]:
        if i !=6 :
            groundtruth = pd.read_csv(input_path + 'new_API_groundtruth.csv')
            prediction = pd.read_csv(input_path +  str(model) + '.csv')

        #         header_device.append(i)
            gt_ = np.array(groundtruth.iloc[:,[i]])
            gt_ = np.where(gt_<= threshold,0,1)
            pred_ = np.array(prediction.iloc[:,[i]])
            pred_ = np.where(pred_<= threshold,0,1)
    #         if i == 2:
    #             sum_ = sum_ + matthews_corrcoef(gt_,pred_,) *ratio[0]
    #         if i == 3:
    #             sum_ = sum_ + matthews_corrcoef(gt_,pred_) *ratio[1]
    #         if i == 4:
    #             sum_ = sum_ + matthews_corrcoef(gt_,pred_) *ratio[2]
    #         if i == 5:
    #             sum_ = sum_ + matthews_corrcoef(gt_,pred_) *ratio[3]

#             if i == 3:
#                 sum_ = sum_ + matthews_corrcoef(gt_,pred_,average='micro') *ratio[0]
#             if i == 5:
#                 sum_ = sum_ + matthews_corrcoef(gt_,pred_,average='micro') *ratio[1]
            if i == 3:
                sum_ = sum_ + f1_score(gt_,pred_,average='micro') *ratio[0]
            if i == 5:
                sum_ = sum_ + f1_score(gt_,pred_,average='micro') *ratio[1]
    #     if i == 6:
    #         groundtruth = pd.read_csv(input_path_2 + 'groundtruth.csv')
    #         prediction = pd.read_csv(input_path_2 +  'FHMM.csv') 
    #         gt_ = np.array(groundtruth.iloc[:,[5]])
    #         gt_ = np.where(gt_<= threshold,0,1)
    #         pred_ = np.array(prediction.iloc[:,[5]])
    #         pred_ = np.where(pred_<= threshold,0,1)
    #         sum_ = sum_ + matthews_corrcoef(gt_,pred_) *ratio[1]
    with open(output_path , 'a') as f:
        writer = csv.writer(f)
        writer.writerow([model,sum_])    

