import warnings
warnings.filterwarnings("ignore")

from nilmtk.api import API

building_number = 3
device_list = ['sockets','light','CE appliance','fridge','waste disposal unit']

data_path = '/aul/homes/qli027/projects/disaggregation/final_version/prepare_for_figures/different_approaches/data/VPN/'

from nilmtk.disaggregate import Mean
from tensorflow import keras 
from nilmtk_contrib.disaggregate import DAE,Seq2Point, Seq2Seq, RNN, WindowGRU
from nilmtk_contrib.disaggregate import AFHMM, AFHMM_SAC
from nilmtk.legacy.disaggregate import CombinatorialOptimisation
# from nilmtk.disaggregate import FHMM_EXACT, Mean
from nilmtk.disaggregate import CO
from nilmtk.api import API
import os

redd = {
  'power': {
    'mains': ['apparent','active'],
    'appliance': ['apparent','active']
  },
  'sample_rate': 1800,

  'appliances': device_list,
 
  'methods': {
    
      'WindowGRU':WindowGRU({'n_epochs':30,'batch_size':1024}),
      'RNN':RNN({'n_epochs':30,'batch_size':1024}),
      'DAE':DAE({'n_epochs':30,'batch_size':1024}),
      'Seq2Point':Seq2Point({'n_epochs':30,'batch_size':1024}),
      'Seq2Seq':Seq2Seq({'n_epochs':30,'batch_size':1024}),
#         'AFHMM': AFHMM({}),
#         'AFHMM_SAC': AFHMM_SAC({}),
        "CO":CO({}),  
#       "FHMM_EXACT":{},
      'Mean': Mean({}),
          
  },
   'train': {    
    'datasets': {
            'Dataport': {
                'path':data_path + '/redd.h5',
				'buildings': {
				building_number: {
					'start_time': '2020-11-27',
					'end_time': '2021-05-19'
				},

				}
				                
			}
			}
	},
	'test': {
	'datasets': {
		'Datport': {
			'path': data_path + '/redd.h5',
			'buildings': {
				building_number: {
					'start_time': '2020-11-27',
					'end_time': '2021-05-19'
				},
			}
	}
},
        'metrics':['rmse']
}
}

api_res = API(redd)

prediction_path = '/aul/homes/qli027/projects/disaggregation/final_version/prepare_for_figures/different_approaches/data/VPN/'
isExist = os.path.exists(prediction_path)
if not isExist:
    os.mkdir(prediction_path)


api_res.gt_overall[device].to_csv(prediction_path + 'new_API_groundtruth.csv')
    
models = ['WindowGRU','RNN','DAE','Seq2Point','Seq2Seq',"CO",'Mean']

for model in models: 
    
    api_res.pred_overall[model][device].to_csv(prediction_path +  model +  '.csv')

    
    
    