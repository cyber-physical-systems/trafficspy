import pandas as pd
import numpy as np
import os
import csv
from sklearn.metrics import mean_squared_error
from math import sqrt
metric = {}
met = 'RMSE'
for house_num in range(3,10):

    models = ['WindowGRU','RNN','DAE','Seq2Point','Seq2Seq',"CO",'Mean']

    input_path = '/aul/homes/qli027/projects/disaggregation/final_version/evaluation/prediction_results/' + str(house_num) + '/'
    output_path = '/aul/homes/qli027/projects/disaggregation/final_version/evaluation/RMSE/'

    isExist = os.path.exists(output_path)
    if not isExist:
        os.mkdir(output_path)
    device_list = ['sockets','light','CE appliance','fridge','waste disposal unit','dish washer',
                   'electric furnace','washer dryer','microwave','smoke alarm','unknown']
    devices = device_list[:house_num]
    header_device = device_list[:house_num]
    header_device.insert(0, "model")
    with open(output_path + str(house_num) +'.csv',  'a') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(header_device)
    csvfile.close()    
    for model in models:
 
        metric['model'] = model
        for device in devices :

            groundtuth = []
            prediction =[]

            groundtuth = pd.read_csv(input_path + 'new_API_groundtruth' + '_' + device + '.csv')  
            prediction = pd.read_csv(input_path + 'new_API_' + model +  '_' +  device + '.csv')

            gt_ = np.array(groundtuth.iloc[:, 1])
            pred_ = np.array(prediction.iloc[:, 1])

            metric[device] = '{0:.6f}'.format(sqrt(mean_squared_error(gt_,pred_)))


        with open(output_path + str(house_num) +'.csv', 'a') as f:
            w = csv.DictWriter(f, header_device)
            w.writerow(metric)


