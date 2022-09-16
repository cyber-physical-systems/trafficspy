import numpy as np
import pandas as pd


input_path = '/aul/homes/qli027/projects/disaggregation/data/N_houses/sample_data/'
output_path = '/aul/homes/qli027/projects/disaggregation/final_version/data/N_houses_sample_with_noise/' 

data = np.random.normal(10000, 2000 , size=470)
data = data.astype(int)

df_ = pd.DataFrame(data, columns=['noise'])

for i in range(3,12):
    
    df = pd.read_csv(input_path  + str(i) + ".csv")
    df["noise"] = df_
    df['sum_'] = df['sum'] + df["noise"]

    df.to_csv(output_path  + str(i) + ".csv", index=False)