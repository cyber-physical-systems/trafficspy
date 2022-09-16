import pandas as pd
import numpy as np
import os
import csv
from sklearn.metrics import mean_squared_error
from math import sqrt
metric = {}
met = 'RMSE'

for house_num in range(3,16):
    rmse = 0

    models = ['FHMM']

    input_path = '/aul/homes/qli027/projects/disaggregation/final_version/data/20_devices/prediction_results/' + str(house_num) + '/'
    output_path = '/aul/homes/qli027/projects/disaggregation/final_version/data/20_devices/prediction_results/RMSE.csv'

#     isExist = os.path.exists(output_path)
#     if not isExist:
#         os.mkdir(output_path)
    
    groundtruth = pd.read_csv(input_path + 'groundtruth.csv')
    prediction = pd.read_csv(input_path +  'FHMM.csv')
    
    for i in range(1,house_num+1):
        gt_ = np.array(groundtruth.iloc[:,[i]])
        pred_ = np.array(prediction.iloc[:,[i]])
        rmse = rmse + sqrt(mean_squared_error(gt_,pred_))
        print(rmse)
    
    rms = rmse / house_num
    print(rms)
    with open(output_path, 'a') as f:
        writer = csv.writer(f)
        writer.writerow([house_num,rms])    
 
    
    
#     device_list = ['Sockets','Light','CE appliance','Fridge','Waste disposal unit','Dish washer',
#                    'Electric furnace','Washer dryer','Microwave','Smoke alarm','Unknown']
#     devices = device_list[:house_num]
#     header_device = device_list[:house_num]
#     header_device.insert(0, "model")

#     for model in models:
 
#         metric['model'] = model
#         for device in devices :

#             groundtuth = []
#             prediction =[]

#             groundtuth = pd.read_csv(input_path + 'groundtruth' + '_' + device + '.csv')  
#             prediction = pd.read_csv(input_path +  model +  '_' +  device + '.csv')


#             gt_ = np.array(groundtuth.iloc[:, 1])
#             pred_ = np.array(prediction.iloc[:, 1])

#             metric[device] = '{0:.6f}'.format(sqrt(mean_squared_error(gt_,pred_)))


#         with open(output_path + str(house_num) +'.csv', 'a') as f:
#             w = csv.DictWriter(f, header_device)
#             w.writerow(metric)


