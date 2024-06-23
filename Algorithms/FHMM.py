import nilmtk
import os
import csv
import time
from matplotlib import rcParams
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from six import iteritems

from nilmtk import DataSet, TimeFrame, MeterGroup, HDFDataStore
from nilmtk.legacy.disaggregate import CombinatorialOptimisation, FHMM
import nilmtk.utils
from nilmtk.legacy.disaggregate.hart_85 import Hart85

building = 3
house_sets = ['first','second','second_1','third','third_1','third_2','forth','forth_1','forth_2','forth_3']
for house in house_sets:
    output_path = '/aul/homes/qli027/projects/disaggregation/final_version/prepare_for_figures/training_time_FHMM/' + str(house) +'.csv'
    for num in range(1,11):
        path = '/aul/homes/qli027/projects/disaggregation/final_version/data/30_devices/REDD/' + str(house) + '/' + str(num) + '/'

        train = DataSet(path + '/redd.h5')
        train.set_window(end="2016-10-12")
        train_elec = train.buildings[building].elec

        mains = train_elec.mains()
        mains_df = next(mains.load())
        # top_5_train_elec = train_elec.submeters().select_top_k(k=house_num)
        def predict(clf, test_elec, sample_period, timezone):
            pred = {}
            gt= {}

            # "ac_type" varies according to the dataset used. 
            # Make sure to use the correct ac_type before using the default parameters in this code.    
            for i, chunk in enumerate(test_elec.mains().load(physical_quantity = 'power', ac_type = 'apparent', sample_period=sample_period)):
                chunk_drop_na = chunk.dropna()
                pred[i] = clf.disaggregate_chunk(chunk_drop_na)
                gt[i]={}

                for meter in test_elec.submeters().meters:
                    # Only use the meters that we trained on (this saves time!)    
                    gt[i][meter] = next(meter.load(physical_quantity = 'power', ac_type = 'active', sample_period=sample_period))
                gt[i] = pd.DataFrame({k:v.squeeze() for k,v in iteritems(gt[i]) if len(v)}, index=next(iter(gt[i].values())).index).dropna()

            # If everything can fit in memory
            gt_overall = pd.concat(gt)
            gt_overall.index = gt_overall.index.droplevel()
            pred_overall = pd.concat(pred)
            pred_overall.index = pred_overall.index.droplevel()

            # Having the same order of columns
            gt_overall = gt_overall[pred_overall.columns]

            #Intersection of index
            gt_index_utc = gt_overall.index.tz_convert("UTC")
            pred_index_utc = pred_overall.index.tz_convert("UTC")
            common_index_utc = gt_index_utc.intersection(pred_index_utc)

            common_index_local = common_index_utc.tz_convert(timezone)
            gt_overall = gt_overall.loc[common_index_local]
            pred_overall = pred_overall.loc[common_index_local]
            appliance_labels = [m for m in gt_overall.columns.values]
            gt_overall.columns = appliance_labels
            pred_overall.columns = appliance_labels
            return gt_overall, pred_overall

        classifiers = {'FHMM':FHMM()}
        predictions = {}
        sample_period = 120
        print("now is house"  + str(house))
        for clf_name, clf in classifiers.items():
            print("*"*20)
            print(clf_name)
            print("*" *20)
            start = time.time()
            # Note that we have given the sample period to downsample the data to 1 minute. 
            # If instead of top_5 we wanted to train on all appliance, we would write 
            # fhmm.train(train_elec, sample_period=60)
            clf.train(train_elec, sample_period=sample_period)

            test = DataSet(path + '/redd.h5')
            test.set_window(start="2016-09-22")
            test_elec = test.buildings[building].elec

            gt, predictions[clf_name] = predict(clf, test_elec, sample_period, train.metadata['timezone'])
            appliance_labels = [m.label() for m in gt.columns.values]
            gt.columns = appliance_labels
            predictions['FHMM'].columns = appliance_labels
            end = time.time()
            print("Runtime =", end-start, "seconds.")
            with open(output_path , 'a') as f:
                writer = csv.writer(f)
                writer.writerow([num,end-start])
