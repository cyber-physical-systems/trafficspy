# this is used to train the model, try different model, generate the csv file of the result

import math
import pandas as pd
import pickle
from sklearn.linear_model import LogisticRegression
from sklearn import metrics
from sklearn import datasets
from sklearn.preprocessing import StandardScaler
import numpy as np
from sklearn.metrics import classification_report, confusion_matrix
import csv
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import PassiveAggressiveClassifier
from sklearn.linear_model import RidgeClassifierCV
import attr
from sklearn import tree
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB

def  knn(X_train, y_train):
    model = KNeighborsClassifier()
    model = model.fit(X_train, y_train)
    return (model)

input_path = '/aul/homes/qli027/projects/disaggregation/final_version/prepare_for_figures/adversary/'
test_path = '/aul/homes/qli027/projects/disaggregation/final_version/prepare_for_figures/adversary/'
output_path = '/aul/homes/qli027/projects/disaggregation/final_version/prepare_for_figures/adversary/mcc.csv'
for i in [20,40,60,80,100]:
    
    data = pd.read_csv(input_path + 'FHMM_' + str(i) + '.csv' )
    data_test = pd.read_csv(test_path +  'FHMM.csv' )
    feature_cols = ['gt']
    X = data[feature_cols]
    test = ['predict']
    y = data.gt_label  # Target variable
    machine = knn(X, y)   # need to choose we use which model
    y_pred = machine.predict(data[feature_cols])
    y_test = data.gt_label

    tn, fp, fn, tp = confusion_matrix(y_test,y_pred).ravel()
    mcc = ((tp * tn) - (fp * fn)) / math.sqrt((tp + fp) * (tp + fn) * (tn + fp) * (tn + fn))

    with open(output_path, 'a') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([str(i), mcc])
    csvfile.close()
