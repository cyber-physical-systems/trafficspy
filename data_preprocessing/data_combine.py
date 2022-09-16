import pandas as pd
import glob

input_path = '/aul/homes/qli027/projects/disaggregation/final_version/data/realdata/1h/'
output_path = '/aul/homes/qli027/projects/disaggregation/final_version/data/realdata/1hour.csv'

header = []

df = pd.read_csv(input_path + '0101' + '.csv')

for name in glob.glob(input_path + '*.csv'):
    
    file_name = name.split('/')[-1]
    if file_name == '0101.csv':
        print(file_name)
    else:       
        df1 = pd.read_csv(name)
        df = [df, df1]
        df = pd.concat(df)
       
df.to_csv(output_path , header=True, mode='a+')


    


    

