# import pandas as pd
# import numpy as np
# import os
# import csv
# from sklearn.metrics import matthews_corrcoef
# from math import sqrt
# metric = {}
# met = 'MCC'
# threshold = 100000
# # for house_num in range(14,16):
# devices = [4322480268,3424383659,1130799754,921227642,684659082]
# sum = 0
# ratio = {}
# for device in devices:
#     sum = sum + device 
# print(sum)
# for i in range(0,5):
#     ratio[i] = devices[i]/sum
# print(ratio)    
# models= ["CO",'RNN','WindowGRU','DAE','Seq2Seq','Mean']
# # models= ["FHMM"]   
# # models = ['FHMM']
# threshold = 1000000
# input_path = '/aul/homes/qli027/projects/disaggregation/final_version/prepare_for_figures/different_approaches/data/VPN_/' 
# output_path = '/aul/homes/qli027/projects/disaggregation/final_version/prepare_for_figures/different_approaches/data/VPN_/mcc_all.csv' 
# input_path_2 = '/aul/homes/qli027/projects/disaggregation/final_version/prepare_for_figures/different_approaches/data/VPN/' 


# for model in models:
#     sum_ = 0
#     for i in [2,3,4,5,6]:
#         if i !=6 :
#             groundtruth = pd.read_csv(input_path + 'new_API_groundtruth.csv')
#             prediction = pd.read_csv(input_path +  str(model) + '.csv')

#         #         header_device.append(i)
#             gt_ = np.array(groundtruth.iloc[:,[i]])
#             gt_ = np.where(gt_<= threshold,0,1)
#             pred_ = np.array(prediction.iloc[:,[i]])
#             pred_ = np.where(pred_<= threshold,0,1)
#             if i == 2:
#                 sum_ = sum_ + matthews_corrcoef(gt_,pred_) *ratio[0]
#             if i == 3:
#                 sum_ = sum_ + matthews_corrcoef(gt_,pred_) *ratio[1]
#             if i == 4:
#                 sum_ = sum_ + matthews_corrcoef(gt_,pred_) *ratio[2]
#             if i == 5:
#                 sum_ = sum_ + matthews_corrcoef(gt_,pred_) *ratio[3]
#         if i == 6:
#             groundtruth = pd.read_csv(input_path_2 + 'new_API_groundtruth.csv')
#             prediction = pd.read_csv(input_path_2 +  str(model) + '.csv') 
#             gt_ = np.array(groundtruth.iloc[:,[3]])
#             gt_ = np.where(gt_<= threshold,0,1)
#             pred_ = np.array(prediction.iloc[:,[3]])
#             pred_ = np.where(pred_<= threshold,0,1)
#             sum_ = sum_ + matthews_corrcoef(gt_,pred_) *ratio[4]
#     with open(output_path , 'a') as f:
#         writer = csv.writer(f)
#         writer.writerow([model,sum_])    
import pandas as pd
import numpy as np
import os
import csv
from sklearn.metrics import matthews_corrcoef
from math import sqrt
metric = {}
met = 'MCC'
threshold = 100000
# for house_num in range(14,16):
devices = [4322480268,3424383659,1130799754,921227642,684659082]
sum = 0
ratio = {}
for device in devices:
    sum = sum + device 
print(sum)
for i in range(0,5):
    ratio[i] = devices[i]/sum
print(ratio)    
# models= ["CO",'RNN','WindowGRU','DAE','Seq2Seq','Mean']
models= ["FHMM"]   
# models = ['FHMM']

input_path = '/aul/homes/qli027/projects/disaggregation/final_version/prepare_for_figures/topk/VPN/predictions/'
output_path = '/aul/homes/qli027/projects/disaggregation/final_version/prepare_for_figures/topk/VPN/predictions/mcc.csv'


mcc ={}
model = 'FHMM'
for threshold in range(0,5000000,5000):
    sum_ = 0
    for i in [1,3,4,5,6,7,8,14,16,18]:

        groundtruth = pd.read_csv(input_path + 'groundtruth.csv')
        prediction = pd.read_csv(input_path +  str(model) + '.csv')

    #         header_device.append(i)
        gt_ = np.array(groundtruth.iloc[:,[i]])
        gt_ = np.where(gt_<= threshold,0,1)
        pred_ = np.array(prediction.iloc[:,[i]])
        pred_ = np.where(pred_<= threshold,0,1)
        mcc[i] = matthews_corrcoef(gt_,pred_) 
#             if i == 2:
#                 sum_ = sum_ + matthews_corrcoef(gt_,pred_) *ratio[0]
#             if i == 3:
#                 sum_ = sum_ + matthews_corrcoef(gt_,pred_) *ratio[1]
#             if i == 4:
#                 sum_ = sum_ + matthews_corrcoef(gt_,pred_) *ratio[2]
#             if i == 5:
#                 sum_ = sum_ + matthews_corrcoef(gt_,pred_) *ratio[3]
       
    with open(output_path , 'a') as f:
        writer = csv.writer(f)
        writer.writerow([threshold, mcc[1],mcc[3],mcc[4],mcc[5],mcc[6],mcc[7],mcc[8],mcc[14],mcc[16],mcc[18]])    


