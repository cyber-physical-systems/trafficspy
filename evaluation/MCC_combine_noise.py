import pandas as pd
devices = ['light','CE appliance','fridge','waste disposal unit','dish washer',
                   'electric furnace','washer dryer','microwave','smoke alarm','unknown']

weights_device = [534856478.0,207843478.0,165481755.0,102623536.0,89811281.0,67620217.0, 48402777.0,34015812.0,31695847.0,24792516.0,24142345.0,17766826.0]

models = ['FHMM']



def weight_calculation(n):

    sum_weights = 0
    sum_list =[]
        
    for i in range(0,n):
        
        sum_weights = sum_weights + weights_device[i]
        

    for j in range(0,n):
        
        sum_list.append(weights_device[j]/sum_weights)

    return(sum_list)

for house_num in range(3,9):
    
    for model in models:
    
        device = [devices[n] for n in range(0,house_num)]


        input_path =  '/aul/homes/qli027/projects/disaggregation/final_version/evaluation/MCC_noise/' + str(house_num) + '/' + model + '.csv'


        output_path =  '/aul/homes/qli027/projects/disaggregation/final_version/evaluation/MCC_combine_noise/'  + str(house_num) + '_' + model + '.csv'


        df = pd.read_csv(input_path)


        df['average' + '_'+ str(house_num)] = df[device].sum(axis=1)/house_num

        weights = weight_calculation(house_num)


        if house_num == 3:
            df['weighted_average'+ '_'+ str(house_num)] =  df['light']*weights[0] + df['CE appliance']*weights[1] + df['fridge']*weights[2]

        if house_num == 4:
            df['weighted_average'+ '_'+ str(house_num)] =  df['light']*weights[0] + df['CE appliance']*weights[1] + df['fridge']*weights[2] + df['waste disposal unit']*weights[3] 

        if house_num == 5:
            df['weighted_average'+ '_'+ str(house_num)] =  df['light']*weights[0] + df['CE appliance']*weights[1] + df['fridge']*weights[2] + df['waste disposal unit']*weights[3] +  df['dish washer']*weights[4] 
            
        if house_num == 6:
            df['weighted_average'+ '_'+ str(house_num)] =  df['light']*weights[0] + df['CE appliance']*weights[1] + df['fridge']*weights[2] + df['waste disposal unit']*weights[3] +  df['dish washer']*weights[4] +  df['electric furnace']*weights[5]

        if house_num == 7:
            df['weighted_average'+ '_'+ str(house_num)] =  df['light']*weights[0] + df['CE appliance']*weights[1] + df['fridge']*weights[2] + df['waste disposal unit']*weights[3] +  df['dish washer']*weights[4] +  df['electric furnace']*weights[5] + df['washer dryer']*weights[6] 
            
        if house_num == 8:
            df['weighted_average'+ '_'+ str(house_num)] =  df['light']*weights[0] + df['CE appliance']*weights[1] + df['fridge']*weights[2] + df['waste disposal unit']*weights[3] +  df['dish washer']*weights[4] +  df['electric furnace']*weights[5] + df['washer dryer']*weights[6]   +   df['microwave']*weights[7] 
            
        if house_num == 9:
            df['weighted_average'+ '_'+ str(house_num)] =  df['light']*weights[0] + df['CE appliance']*weights[1] + df['fridge']*weights[2] + df['waste disposal unit']*weights[3] +  df['dish washer']*weights[4] +  df['electric furnace']*weights[5] + df['washer dryer']*weights[6]   +   df['microwave']*weights[7] +  df['smoke alarm']*weights[8]   
            
        if house_num == 10:
            df['weighted_average'+ '_'+ str(house_num)] =  df['light']*weights[0] + df['CE appliance']*weights[1] + df['fridge']*weights[2] + df['waste disposal unit']*weights[3] +  df['dish washer']*weights[4] +  df['electric furnace']*weights[5] + df['washer dryer']*weights[6]   +   df['microwave']*weights[7] +  df['smoke alarm']*weights[8]    + df['unknown']*weights[9]          

        df.to_csv(output_path, header=True)

for model in models: 
    house_num =3
    input_path = '/aul/homes/qli027/projects/disaggregation/final_version/evaluation/MCC_combine_noise/'  + str(house_num) + '_' + model + '.csv'
    output_path =  '/aul/homes/qli027/projects/disaggregation/final_version/evaluation/MCC_diff_algorithm_noise/' + model + '.csv'
   
    df = pd.read_csv(input_path)

    columns = ['threshold','average_3','weighted_average_3']
    df1 = df.loc[:, columns]

    for house_num in range(4,9):
        input_path =  '/aul/homes/qli027/projects/disaggregation/final_version/evaluation/MCC_combine_noise/'  + str(house_num) + '_' + model + '.csv'
        df = pd.read_csv(input_path)
        df1['average_' + str(house_num)] = df['average_' + str(house_num)]
        df1['weighted_average_' + str(house_num)] = df['weighted_average_' + str(house_num)]
    df1.to_csv(output_path, header=True,index = False)    
