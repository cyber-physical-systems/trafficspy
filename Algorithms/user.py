# this is used to train the model, try different model, generate the csv file of the result

import math
import pandas as pd
import pickle
from sklearn import metrics
from sklearn import datasets
from sklearn.preprocessing import StandardScaler
import numpy as np
from sklearn.metrics import classification_report, confusion_matrix
import csv

models = ["CO",'RNN','WindowGRU','DAE','Seq2Seq','Mean','FHMM']
devices = ['Sockets','Light','CE appliance','Fridge','Waste disposal unit','Dish washer','Electric furnace','Microwave',
          'Smoke alarm','Unknown']
device = ['sockets','light','CE appliance','fridge','waste disposal unit','dish washer','electric furnace','microwave','smoke alarm','unknown']
input_path = '/aul/homes/qli027/projects/disaggregation/final_version/prepare_for_figures/user_activity/VPN/'
output_path = '/aul/homes/qli027/projects/disaggregation/final_version/prepare_for_figures/user_activity/evaluation/VPN/'
for i in range(0,10):
    for model in models:
        if model == 'FHMM' :
            data = pd.read_csv(input_path + str(devices[i]) + '/'  + str(model) + '.csv' ,index_col=[0])
            y_test = data['gt_label']
            y_pred = data['predict_label']

            tn, fp, fn, tp = confusion_matrix(y_test,y_pred).ravel()
            mcc = ((tp * tn) - (fp * fn)) / math.sqrt((tp + fp) * (tp + fn) * (tn + fp) * (tn + fn))

            with open(output_path + str(devices[i]) + '.csv', 'a') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow([model, tn, fp, fn, tp, mcc])
            csvfile.close()
        else:
            data = pd.read_csv(input_path + str(device[i]) + '/'  + str(model) + '.csv' ,index_col=[0])
            y_test = data['gt_label']
            y_pred = data['predict_label']

            tn, fp, fn, tp = confusion_matrix(y_test,y_pred).ravel()
            mcc = ((tp * tn) - (fp * fn)) / math.sqrt((tp + fp) * (tp + fn) * (tn + fp) * (tn + fn))

            with open(output_path + str(device[i]) + '.csv', 'a') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow([model, tn, fp, fn, tp, mcc])
            csvfile.close()            
