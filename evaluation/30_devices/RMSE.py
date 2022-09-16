import pandas as pd
import numpy as np
import os
import csv
from sklearn.metrics import mean_squared_error
from math import sqrt
metric = {}
met = 'RMSE'

for house_num in range(1,11):
    rmse = 0

    models = ['FHMM']

    input_path = '/aul/homes/qli027/projects/disaggregation/final_version/data/30_devices/prediction_results/first/' + str(house_num) + '/'
    output_path = '/aul/homes/qli027/projects/disaggregation/final_version/data/30_devices/prediction_results/RMSE.csv'

#     isExist = os.path.exists(output_path)
#     if not isExist:
#         os.mkdir(output_path)
    
    groundtruth = pd.read_csv(input_path + 'groundtruth.csv')
    prediction = pd.read_csv(input_path +  'FHMM.csv')
    
    for i in range(1,house_num+1):
        gt_ = np.array(groundtruth.iloc[:,[i]])
        pred_ = np.array(prediction.iloc[:,[i]])
        rmse = rmse + sqrt(mean_squared_error(gt_,pred_))

    
    rms = rmse / house_num
    print(rms)
    with open(output_path, 'a') as f:
        writer = csv.writer(f)
        writer.writerow([house_num,rms])    

        
for house_num in range(11,21):
    rmse = 0

    models = ['FHMM']
    
    for j in range(1,11):
        
        input_path = '/aul/homes/qli027/projects/disaggregation/final_version/data/30_devices/prediction_results/second_1/' + str(j) + '/'


        groundtruth = pd.read_csv(input_path + 'groundtruth.csv')
        prediction = pd.read_csv(input_path +  'FHMM.csv')
        gt_ = np.array(groundtruth.iloc[:,[j]])
        pred_ = np.array(prediction.iloc[:,[j]])
        rmse = rmse + sqrt(mean_squared_error(gt_,pred_))
    
    for i in range(1,house_num+1-10):
        input_path = '/aul/homes/qli027/projects/disaggregation/final_version/data/30_devices/prediction_results/second/' + str(i) + '/'

        groundtruth = pd.read_csv(input_path + 'groundtruth.csv')
        prediction = pd.read_csv(input_path +  'FHMM.csv')
        gt_ = np.array(groundtruth.iloc[:,[i]])
        pred_ = np.array(prediction.iloc[:,[i]])
        rmse = rmse + sqrt(mean_squared_error(gt_,pred_))
        print(rmse)
    
    rms = rmse / house_num
    print(rms)
    with open(output_path, 'a') as f:
        writer = csv.writer(f)
        writer.writerow([house_num,rms])    
 
for house_num in range(21,31):
    rmse = 0

    models = ['FHMM']
    for j in range(1,11):
        
        input_path = '/aul/homes/qli027/projects/disaggregation/final_version/data/30_devices/prediction_results/third_1/' + str(j) + '/'


        groundtruth = pd.read_csv(input_path + 'groundtruth.csv')
        prediction = pd.read_csv(input_path +  'FHMM.csv')
        gt_ = np.array(groundtruth.iloc[:,[j]])
        pred_ = np.array(prediction.iloc[:,[j]])
        rmse = rmse + sqrt(mean_squared_error(gt_,pred_))
        
    for k in range(1,11):
        
        input_path = '/aul/homes/qli027/projects/disaggregation/final_version/data/30_devices/prediction_results/third_2/' + str(k) + '/'


        groundtruth = pd.read_csv(input_path + 'groundtruth.csv')
        prediction = pd.read_csv(input_path +  'FHMM.csv')
        gt_ = np.array(groundtruth.iloc[:,[k]])
        pred_ = np.array(prediction.iloc[:,[k]])
        rmse = rmse + sqrt(mean_squared_error(gt_,pred_))  
        
    for i in range(1,house_num+1-20):
        input_path = '/aul/homes/qli027/projects/disaggregation/final_version/data/30_devices/prediction_results/third/' + str(i) + '/'

        groundtruth = pd.read_csv(input_path + 'groundtruth.csv')
        prediction = pd.read_csv(input_path +  'FHMM.csv')
        gt_ = np.array(groundtruth.iloc[:,[i]])
        pred_ = np.array(prediction.iloc[:,[i]])
        rmse = rmse + sqrt(mean_squared_error(gt_,pred_))
        print(rmse)
    
    rms = rmse / house_num
    print(rms)
    with open(output_path, 'a') as f:
        writer = csv.writer(f)
        writer.writerow([house_num,rms]) 
    
for house_num in range(31,41):
    rmse = 0

    models = ['FHMM']
    for j in range(1,11):
        
        input_path = '/aul/homes/qli027/projects/disaggregation/final_version/data/30_devices/prediction_results/forth_1/' + str(j) + '/'


        groundtruth = pd.read_csv(input_path + 'groundtruth.csv')
        prediction = pd.read_csv(input_path +  'FHMM.csv')
        gt_ = np.array(groundtruth.iloc[:,[j]])
        pred_ = np.array(prediction.iloc[:,[j]])
        rmse = rmse + sqrt(mean_squared_error(gt_,pred_))
        
    for k in range(1,11):
        
        input_path = '/aul/homes/qli027/projects/disaggregation/final_version/data/30_devices/prediction_results/forth_2/' + str(k) + '/'


        groundtruth = pd.read_csv(input_path + 'groundtruth.csv')
        prediction = pd.read_csv(input_path +  'FHMM.csv')
        gt_ = np.array(groundtruth.iloc[:,[k]])
        pred_ = np.array(prediction.iloc[:,[k]])
        rmse = rmse + sqrt(mean_squared_error(gt_,pred_))  
        
    for m in range(1,11):
        
        input_path = '/aul/homes/qli027/projects/disaggregation/final_version/data/30_devices/prediction_results/forth_3/' + str(m) + '/'


        groundtruth = pd.read_csv(input_path + 'groundtruth.csv')
        prediction = pd.read_csv(input_path +  'FHMM.csv')
        gt_ = np.array(groundtruth.iloc[:,[m]])
        pred_ = np.array(prediction.iloc[:,[m]])
        rmse = rmse + sqrt(mean_squared_error(gt_,pred_))   
        
    for i in range(1,house_num+1-30):
        input_path = '/aul/homes/qli027/projects/disaggregation/final_version/data/30_devices/prediction_results/forth/' + str(i) + '/'

        groundtruth = pd.read_csv(input_path + 'groundtruth.csv')
        prediction = pd.read_csv(input_path +  'FHMM.csv')
        gt_ = np.array(groundtruth.iloc[:,[i]])
        pred_ = np.array(prediction.iloc[:,[i]])
        rmse = rmse + sqrt(mean_squared_error(gt_,pred_))
        print(rmse)

    rms = rmse / house_num
    print(rms)
    with open(output_path, 'a') as f:
        writer = csv.writer(f)
        writer.writerow([house_num,rms])    
