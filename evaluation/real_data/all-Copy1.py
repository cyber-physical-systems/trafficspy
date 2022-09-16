import pandas as pd
import numpy as np
import os
import csv
from sklearn.metrics import mean_squared_error
from sklearn.metrics import matthews_corrcoef
from math import sqrt
metric = {}
met = 'RMSE'
threshold = 970000
def percentage_error(actual, predicted):
    res = np.empty(actual.shape)
    for j in range(actual.shape[0]):
        if actual[j] != 0:
            res[j] = (actual[j] - predicted[j]) / actual[j]
        else:
            res[j] = predicted[j] / np.mean(actual)
    return res

def Mean_absolute_percentage_error(y_true, y_pred): 
    return np.mean(np.abs(percentage_error(np.asarray(y_true), np.asarray(y_pred)))) 
house_num = 5
models= ["CO",'RNN','WindowGRU','DAE','Seq2Seq','Mean']
# models= ["FHMM"]


for model in models:

    rmse = 0
    mape = 0 
    sum_  = 0
    rmse ={}
    mape = {}
    input_path = '/aul/homes/qli027/projects/disaggregation/final_version/prepare_for_figures/different_approaches/data/VPN/' 
    output_path = '/aul/homes/qli027/projects/disaggregation/final_version/prepare_for_figures/different_approaches/data/VPN/evaluation.csv'

#     isExist = os.path.exists(output_path)
#     if not isExist:
#         os.mkdir(output_path)

    groundtruth = pd.read_csv(input_path + 'new_API_groundtruth.csv')
    prediction = pd.read_csv(input_path + str(model) +  '.csv')

#     for i in range(2,house_num-2):
#     for i in range(1,house_num+1):
#     for i in [3,4,5]:
    for i in [1,2,3,4,5]:
        gt_ = np.array(groundtruth.iloc[:,[i]])
        pred_ = np.array(prediction.iloc[:,[i]])
#         rmse = rmse + sqrt(mean_squared_error(gt_,pred_))
#         mape = mape + Mean_absolute_percentage_error(gt_,pred_)
#         gt_ = np.where(gt_<= threshold,0,1)
#         pred_ = np.where(pred_<= threshold,0,1)
#         sum_ = sum_ + matthews_corrcoef(gt_,pred_)
        rmse[i] =  sqrt(mean_squared_error(gt_,pred_))
        mape[i] =  Mean_absolute_percentage_error(gt_,pred_)
        

#     rms = rmse / 4
#     MAP = mape / 4
#     mcc =  sum_ / house_num  
#     rms = rmse 
#     MAP = mape 
#     mcc =  sum_ 
#     print(model,mcc)
#     with open(output_path , 'a') as f:
#         writer = csv.writer(f)
#         writer.writerow([model,rms,MAP])    
    with open(output_path , 'a') as f:
        writer = csv.writer(f)
        writer.writerow([model,mape[1],mape[2],mape[3],mape[4],mape[5]])    
