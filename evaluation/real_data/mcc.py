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

models = ['FHMM']

input_path = '/aul/homes/qli027/projects/disaggregation/final_version/prepare_for_figures/different_approaches/data/VPN/' 
output_path = '/aul/homes/qli027/projects/disaggregation/final_version/prepare_for_figures/different_approaches/data/VPN/mcc.csv' 

# isExist = os.path.exists(output_path)
# if not isExist:
#     os.mkdir(output_path)

groundtruth = pd.read_csv(input_path + 'groundtruth.csv')
prediction = pd.read_csv(input_path +  'FHMM.csv')
threshold = 970000
# for threshold in range(0,5000000,10000):
# models= ["CO",'RNN','WindowGRU','DAE','Seq2Seq','Mean','FHMM']
# for model in models:
#     metric['threshold'] = threshold
#     header_device = ['threshold']
#     header_device = model
sum_ = 0
for i in [3,4,5]:

#         header_device.append(i)
    gt_ = np.array(groundtruth.iloc[:,[i]])
    gt_ = np.where(gt_<= threshold,0,1)
    pred_ = np.array(prediction.iloc[:,[i]])
    pred_ = np.where(pred_<= threshold,0,1)
#         metric[i] = '{0:.6f}'.format(matthews_corrcoef(gt_,pred_))
#         if i == 2:
#             sum_ = sum_ + matthews_corrcoef(gt_,pred_) *0.4183
#         if i == 3:
#             sum_ = sum_ + matthews_corrcoef(gt_,pred_) *0.3238
#         if i ==5:
#             sum_ = sum_ + matthews_corrcoef(gt_,pred_) *0.2579   
    if i == 3:
        sum_ = sum_ + matthews_corrcoef(gt_,pred_) *0.4132
    if i == 4:
        sum_ = sum_ + matthews_corrcoef(gt_,pred_) *0.3366
    if i ==5:
        sum_ = sum_ + matthews_corrcoef(gt_,pred_) *0.2502 

#     metric['average'] =  sum_
#     with open(output_path + 'mcc.csv', 'a') as f:
#         w = csv.DictWriter(f, header_device)
#         w.writerow(metric)
    with open(output_path , 'a') as f:
        writer = csv.writer(f)
        writer.writerow([threshold,sum_])    

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

# models = ['FHMM']

# input_path = '/aul/homes/qli027/projects/disaggregation/final_version/prepare_for_figures/different_approaches/data/UNSW/' 
# output_path = '/aul/homes/qli027/projects/disaggregation/final_version/prepare_for_figures/different_approaches/data/UNSW/mcc.csv' 

# # isExist = os.path.exists(output_path)
# # if not isExist:
# #     os.mkdir(output_path)

# # groundtruth = pd.read_csv(input_path + 'groundtruth.csv')
# # prediction = pd.read_csv(input_path +  'FHMM.csv')

# # for threshold in range(0,1000000,50000):
# models= ['FHMM',"CO",'RNN','WindowGRU','DAE','Seq2Seq','Mean','FHMM']
# for model in models:
    
#     groundtruth = pd.read_csv(input_path + 'groundtruth.csv')
#     prediction = pd.read_csv(input_path +  str(model) + '.csv')

#     header_device = model
#     sum_ = 0
#     for i in [2,3,5]:

   
#         gt_ = np.array(groundtruth.iloc[:,[i]])
#         gt_ = np.where(gt_<= threshold,0,1)
#         pred_ = np.array(prediction.iloc[:,[i]])
#         pred_ = np.where(pred_<= threshold,0,1)
#         metric[i] = '{0:.6f}'.format(matthews_corrcoef(gt_,pred_))
#         if i == 2:
#             sum_ = sum_ + matthews_corrcoef(gt_,pred_) *0.4183
#         if i == 3:
#             sum_ = sum_ + matthews_corrcoef(gt_,pred_) *0.3238
#         if i ==5:
#             sum_ = sum_ + matthews_corrcoef(gt_,pred_) *0.2579   
            

#     with open(output_path , 'a') as f:
#         writer = csv.writer(f)
#         writer.writerow([model,sum_])    



