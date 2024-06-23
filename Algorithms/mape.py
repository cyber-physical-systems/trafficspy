import pandas as pd
import numpy as np
import os
import csv
from sklearn.metrics import mean_squared_error
from sklearn.metrics import matthews_corrcoef
from sklearn.metrics import mean_absolute_error
from math import sqrt
metric = {}
met = 'RMSE'
# threshold = 400000
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

periods = ['1min','3min','5min','10min','30min','1h']
for period in periods :
    mape = {}
    for model in models:

        rmse = 0
        
        sum_  = 0
        rmse ={}
       
        mae = {}
        input_path =  '/aul/homes/qli027/projects/disaggregation/final_version/prepare_for_figures/noise/VPN/prediction/' + str(period) + '/' 
        output_path = '/aul/homes/qli027/projects/disaggregation/final_version/prepare_for_figures/noise/VPN/prediction/mape_all.csv'

    #     isExist = os.path.exists(output_path)
    #     if not isExist:
    #         os.mkdir(output_path)

        groundtruth = pd.read_csv(input_path + 'new_API_groundtruth.csv')
        prediction = pd.read_csv(input_path + str(model) +  '.csv')

#         for i in range(1,6):
#         for i in [3,4,5,6]:
        for i in [4]:
 
            gt_ = np.array(groundtruth.iloc[:,[i]])
            pred_ = np.array(prediction.iloc[:,[i]])

            rmse[i] =  sqrt(mean_squared_error(gt_,pred_))
#             mape[i] =  Mean_absolute_percentage_error(gt_,pred_)
            mape[model] = Mean_absolute_percentage_error(gt_,pred_)
#     print(mape)
    #         mae[i] = mean_absolute_error(gt_,pred_)
#         mape_all = (mape[1]+ mape[2]+mape[3]+mape[4]+mape[5])/5
#         mape_all = (mape[3]+ mape[4]+mape[5]+mape[6]+mape[7])/5
# models= ["CO",'RNN','WindowGRU','DAE','Seq2Seq','Mean']
    with open(output_path , 'a') as f:
        writer = csv.writer(f)
        writer.writerow([period,mape['CO'],mape['RNN'],mape['WindowGRU'],mape['DAE'],mape['Seq2Seq'],mape['Mean']])
    #         writer.writerow([model,mape[1],mape[3],mape[4],mape[5],mape[6],mape[7],mape[8],mape[14],mape[16], mape[18]]) 
#             writer.writerow([period,model,mape[1],mape[2],mape[3],mape[4],mape[5],mape_all]) 
#             writer.writerow([period,model,mape[3],mape[4],mape[5],mape[6],mape[7],mape_all])

