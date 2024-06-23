import numpy as np
import pandas as pd


input_path = '/aul/homes/qli027/projects/disaggregation/final_version/prepare_for_figures/diff_granularity/data/UNSW/'
output_path = '/aul/homes/qli027/projects/disaggregation/final_version/prepare_for_figures/noise/UNSW/' 

data = np.random.normal(10000, 5000 , size=14341)
data = data.astype(int)

df_ = pd.DataFrame(data, columns=['noise'])

df = pd.read_csv(input_path  + "1min.csv")
columns = ['TIME','DropcamOut','LaptopOut','WelcomeOut']
df1 = df.loc[:, columns]
df1["noise"] = df_
df1['sum'] =  df1["noise"]+ df["DropcamOut"] + df["LaptopOut"] + df["WelcomeOut"]

df1.to_csv(output_path  + "4.csv", index=False)