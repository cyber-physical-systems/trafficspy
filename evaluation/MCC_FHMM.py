import pandas as pd
import numpy as np
import os
import csv
from sklearn.metrics import matthews_corrcoef

met = 'MCC'
for house_num in range(3,9):
    models = ['FHMM']
    input_path = '/aul/homes/qli027/projects/disaggregation/final_version/evaluation/prediction_results_test_seperately/' + str(house_num) + '/'
    output_path = '/aul/homes/qli027/projects/disaggregation/final_version/evaluation/MCC_test_seperately/' + str(house_num) + '/'

    isExist = os.path.exists(output_path)
    if not isExist:
        os.mkdir(output_path)

#     device_list = ['Sockets','Light','CE appliance','Fridge','Waste disposal unit','Dish washer',
#                    'Electric furnace','Washer dryer','Microwave','Smoke alarm','Unknown']
    device_list = ['Sockets','Light','CE appliance','Fridge','Waste disposal unit','Dish washer',
                   'Electric furnace','Washer dryer','Microwave','Smoke alarm','Unknown']
    
    devices = device_list[:house_num]
    
    header_device = device_list[:house_num]
    header_device.insert(0, "threshold")

    for model in models:

        metric = {}

        with open(output_path + model +'.csv',  'a') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(header_device)
        csvfile.close()    


        for threshold in range(1000,295000,100):

            for device in devices :

                metric['threshold'] = threshold
                groundtuth = []
                prediction =[]

                groundtuth = pd.read_csv(input_path + 'groundtruth' + '_' + device + '.csv')  
                prediction = pd.read_csv(input_path +  model +  '_' +  device + '.csv')

                gt_ = np.array(groundtuth.iloc[:, 1])
                gt_ = np.where(gt_<= threshold,0,1)
                pred_ = np.array(prediction.iloc[:, 1])
                pred_ = np.where(pred_<= threshold,0,1)

                metric[device] = '{0:.6f}'.format(matthews_corrcoef(gt_,pred_))


            with open(output_path + model +'.csv', 'a') as f:
                w = csv.DictWriter(f, header_device)
                w.writerow(metric)

