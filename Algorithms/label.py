import pandas as pd
import os
import csv
import glob

input_path = '/aul/homes/qli027/projects/disaggregation/final_version/prepare_for_figures/topk/VPN/predictions/'
output_path = '/aul/homes/qli027/projects/disaggregation/final_version/prepare_for_figures/user_activity/VPN/'

models = ["CO",'RNN','WindowGRU','DAE','Seq2Seq','Mean','FHMM']
# thresholds = [600000,0,100000,20000,0,200000,100000,0,0,50000]
thresholds = [0,500000,200000,30000,10000,1000,10000,0,0,0]

# thresholds = [10000,0,1000,1000,0]
devices = ['Sockets','Light','CE appliance','Fridge','Waste disposal unit','Dish washer','Electric furnace','Microwave',
          'Smoke alarm','Unknown']
device = ['sockets','light','CE appliance','fridge','waste disposal unit','dish washer','electric furnace','microwave','smoke alarm','unknown']
for model in models:
    if model == 'FHMM' :
        groundtruth = pd.read_csv(input_path + 'groundtruth.csv',index_col=[0])
        prediction = pd.read_csv(input_path + str(model) + '.csv',index_col=[0])
        for i in range(0,10):
            prediction_path = output_path + str(devices[i]) + '/'
            isExist = os.path.exists(prediction_path)
            if not isExist:
                os.mkdir(prediction_path)
            df1 = groundtruth.loc[:,devices[i]]
            
            df1 = pd.concat([df1,prediction[devices[i]]], axis=1)
            col = ['gt', 'predict']
            df1.columns = col

            #df1['prediction'] = prediction[devices[i]]
            
            df1.reset_index(drop=True, inplace=True)
#             print(df1['prediction'])
            df1['gt_label'] = 0
            for j in range (0,len(df1)):
                if df1.iloc[j]['gt'] > thresholds[i]:
                    df1.loc[i]['gt_label'] = 1
            df1['gt_label'][df1['gt'] > thresholds[i]]= 1
            
            df1['predict_label'] = 0
            for j in range (0,len(df1)):
                if df1.iloc[j]['predict'] > thresholds[i]:
                    df1.loc[i]['predict_label'] = 1
            df1['predict_label'][df1['predict'] > thresholds[i]]= 1
            
            df1.to_csv(prediction_path + str(model) + '.csv', header=True,index = False, mode='a+')
    else:
        groundtruth = pd.read_csv(input_path + 'new_API_groundtruth.csv',index_col=[0])
        prediction = pd.read_csv(input_path + str(model) + '.csv',index_col=[0])
        for i in range(0,10):
            prediction_path = output_path + str(device[i]) + '/'
            isExist = os.path.exists(prediction_path)
            if not isExist:
                os.mkdir(prediction_path)
            df1 = groundtruth.loc[:,device[i]]
            
            df1 = pd.concat([df1,prediction[device[i]]], axis=1)
            col = ['gt', 'predict']
            df1.columns = col
            
            df1.reset_index(drop=True, inplace=True)

            df1['gt_label'] = 0
            for j in range (0,len(df1)):
                if df1.iloc[j]['gt'] > thresholds[i]:
                    df1.loc[i]['gt_label'] = 1
            df1['gt_label'][df1['gt'] > thresholds[i]]= 1
            
            df1['predict_label'] = 0
            for j in range (0,len(df1)):
                if df1.iloc[j]['predict'] > thresholds[i]:
                    df1.loc[i]['predict_label'] = 1
            df1['predict_label'][df1['predict'] > thresholds[i]]= 1
            
            df1.to_csv(prediction_path + str(model) + '.csv', header=True,index = False, mode='a+')
        
    
            