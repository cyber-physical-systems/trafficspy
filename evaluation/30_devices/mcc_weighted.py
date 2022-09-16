import pandas as pd
import numpy as np
import os
import csv
from sklearn.metrics import matthews_corrcoef
from math import sqrt
metric = {}
met = 'mcc'
threshold = 3430000
sort_device = '/aul/homes/qli027/projects/disaggregation/final_version/data/30_devices/sorted_device.csv'
df_device = pd.read_csv(sort_device)
devices= df_device['sum'].tolist()
print(devices)

for house_num in range(1,11):
    rmse = 0
    ratio = {}
    sum_ = 0
    for num in range(0,house_num): 
        sum_ = sum_ + devices[num] 
    print(sum_)
    for num in range(0,house_num):
        ratio[num] = devices[num]/sum_
    print(ratio) 

    models = ['FHMM']

    input_path = '/aul/homes/qli027/projects/disaggregation/final_version/data/30_devices/prediction_results/first/' + str(house_num) + '/'
    output_path = '/aul/homes/qli027/projects/disaggregation/final_version/data/30_devices/prediction_results/mcc_weighted.csv'


    groundtruth = pd.read_csv(input_path + 'groundtruth.csv')
    prediction = pd.read_csv(input_path +  'FHMM.csv')

    for i in range(1,house_num+1):
        gt_ = np.array(groundtruth.iloc[:,[i]])
        gt_ = np.where(gt_<= threshold,0,1)
        pred_ = np.array(prediction.iloc[:,[i]])
        pred_ = np.where(pred_<= threshold,0,1)

        rmse = rmse + matthews_corrcoef(gt_,pred_)*ratio[i-1]
        print(rmse)


#     rms = rmse / house_num
#     print(rms)
    with open(output_path, 'a') as f:
        writer = csv.writer(f)
        writer.writerow([house_num,rmse])    

        
for house_num in range(11,21):
    rmse = 0
    ratio = {}
    sum_ = 0
    for num in range(0,house_num): 
        sum_ = sum_ + devices[num] 
    print(sum_)
    for num in range(0,house_num):
        ratio[num] = devices[num]/sum_
    print(ratio) 
    models = ['FHMM']
    
    for j in range(1,11):
        
        input_path = '/aul/homes/qli027/projects/disaggregation/final_version/data/30_devices/prediction_results/second_1/' + str(j) + '/'


        groundtruth = pd.read_csv(input_path + 'groundtruth.csv')
        prediction = pd.read_csv(input_path +  'FHMM.csv')
        gt_ = np.array(groundtruth.iloc[:,[j]])
        gt_ = np.where(gt_<= threshold,0,1)
        pred_ = np.array(prediction.iloc[:,[j]])
        pred_ = np.where(pred_<= threshold,0,1)

        rmse = rmse + matthews_corrcoef(gt_,pred_)*ratio[j-1]

    
    for i in range(1,house_num+1-10):
        input_path = '/aul/homes/qli027/projects/disaggregation/final_version/data/30_devices/prediction_results/second/' + str(i) + '/'

        groundtruth = pd.read_csv(input_path + 'groundtruth.csv')
        prediction = pd.read_csv(input_path +  'FHMM.csv')
        gt_ = np.array(groundtruth.iloc[:,[i]])
        gt_ = np.where(gt_<= threshold,0,1)
        pred_ = np.array(prediction.iloc[:,[i]])
        pred_ = np.where(pred_<= threshold,0,1)

        rmse = rmse + matthews_corrcoef(gt_,pred_)*ratio[i+9]

       
    with open(output_path, 'a') as f:
        writer = csv.writer(f)
        writer.writerow([house_num,rmse])    
 
for house_num in range(21,31):
    rmse = 0
    ratio = {}
    sum_ = 0
    for num in range(0,house_num): 
        sum_ = sum_ + devices[num] 
    print(sum_)
    for num in range(0,house_num):
        ratio[num] = devices[num]/sum_
    print(ratio) 
    models = ['FHMM']
    for j in range(1,11):
        
        input_path = '/aul/homes/qli027/projects/disaggregation/final_version/data/30_devices/prediction_results/third_1/' + str(j) + '/'


        groundtruth = pd.read_csv(input_path + 'groundtruth.csv')
        prediction = pd.read_csv(input_path +  'FHMM.csv')
        gt_ = np.array(groundtruth.iloc[:,[j]])
        gt_ = np.where(gt_<= threshold,0,1)
        pred_ = np.array(prediction.iloc[:,[j]])
        pred_ = np.where(pred_<= threshold,0,1)

        rmse = rmse + matthews_corrcoef(gt_,pred_)*ratio[j-1]

        
    for k in range(1,11):
        
        input_path = '/aul/homes/qli027/projects/disaggregation/final_version/data/30_devices/prediction_results/third_2/' + str(k) + '/'


        groundtruth = pd.read_csv(input_path + 'groundtruth.csv')
        prediction = pd.read_csv(input_path +  'FHMM.csv')
        gt_ = np.array(groundtruth.iloc[:,[k]])
        gt_ = np.where(gt_<= threshold,0,1)
        pred_ = np.array(prediction.iloc[:,[k]])
        pred_ = np.where(pred_<= threshold,0,1)

        rmse = rmse + matthews_corrcoef(gt_,pred_)*ratio[k+9]

        
    for i in range(1,house_num+1-20):
        input_path = '/aul/homes/qli027/projects/disaggregation/final_version/data/30_devices/prediction_results/third/' + str(i) + '/'

        groundtruth = pd.read_csv(input_path + 'groundtruth.csv')
        prediction = pd.read_csv(input_path +  'FHMM.csv')
        gt_ = np.array(groundtruth.iloc[:,[i]])
        gt_ = np.where(gt_<= threshold,0,1)
        pred_ = np.array(prediction.iloc[:,[i]])
        pred_ = np.where(pred_<= threshold,0,1)

        rmse = rmse + matthews_corrcoef(gt_,pred_)*ratio[i+19]


    with open(output_path, 'a') as f:
        writer = csv.writer(f)
        writer.writerow([house_num,rmse]) 
    
for house_num in range(31,41):
    rmse = 0
    ratio = {}
    sum_ = 0
    for num in range(0,house_num): 
        sum_ = sum_ + devices[num] 
    print(sum_)
    for num in range(0,house_num):
        ratio[num] = devices[num]/sum_
    print(ratio) 
    models = ['FHMM']
    for j in range(1,11):
        
        input_path = '/aul/homes/qli027/projects/disaggregation/final_version/data/30_devices/prediction_results/forth_1/' + str(j) + '/'


        groundtruth = pd.read_csv(input_path + 'groundtruth.csv')
        prediction = pd.read_csv(input_path +  'FHMM.csv')
        gt_ = np.array(groundtruth.iloc[:,[j]])
        gt_ = np.where(gt_<= threshold,0,1)
        pred_ = np.array(prediction.iloc[:,[j]])
        pred_ = np.where(pred_<= threshold,0,1)

        rmse = rmse + matthews_corrcoef(gt_,pred_)*ratio[j-1]

        
    for k in range(1,11):
        
        input_path = '/aul/homes/qli027/projects/disaggregation/final_version/data/30_devices/prediction_results/forth_2/' + str(k) + '/'


        groundtruth = pd.read_csv(input_path + 'groundtruth.csv')
        prediction = pd.read_csv(input_path +  'FHMM.csv')
        gt_ = np.array(groundtruth.iloc[:,[k]])
        gt_ = np.where(gt_<= threshold,0,1)
        pred_ = np.array(prediction.iloc[:,[k]])
        pred_ = np.where(pred_<= threshold,0,1)

        rmse = rmse + matthews_corrcoef(gt_,pred_)*ratio[k+9]

        
    for m in range(1,11):
        
        input_path = '/aul/homes/qli027/projects/disaggregation/final_version/data/30_devices/prediction_results/forth_3/' + str(m) + '/'


        groundtruth = pd.read_csv(input_path + 'groundtruth.csv')
        prediction = pd.read_csv(input_path +  'FHMM.csv')
        gt_ = np.array(groundtruth.iloc[:,[m]])
        gt_ = np.where(gt_<= threshold,0,1)
        pred_ = np.array(prediction.iloc[:,[m]])
        pred_ = np.where(pred_<= threshold,0,1)

        rmse = rmse + matthews_corrcoef(gt_,pred_)*ratio[m+19]

        
    for i in range(1,house_num+1-30):
        input_path = '/aul/homes/qli027/projects/disaggregation/final_version/data/30_devices/prediction_results/forth/' + str(i) + '/'

        groundtruth = pd.read_csv(input_path + 'groundtruth.csv')
        prediction = pd.read_csv(input_path +  'FHMM.csv')
        gt_ = np.array(groundtruth.iloc[:,[i]])
        gt_ = np.where(gt_<= threshold,0,1)
        pred_ = np.array(prediction.iloc[:,[i]])
        pred_ = np.where(pred_<= threshold,0,1)

        rmse = rmse + matthews_corrcoef(gt_,pred_)*ratio[i+29]

    with open(output_path, 'a') as f:
        writer = csv.writer(f)
        writer.writerow([house_num,rmse])    
