from nilmtk.dataset_converters import convert_redd
import os

for house_num in range(4,5):

    input_path = '/aul/homes/qli027/projects/disaggregation/final_version/data/N_houses/low_freq/house_3/'
    import os

    for i in range(1,23):
        file_path = input_path + 'channel_' + str(i) + '.dat'
        if os.path.exists(file_path):
            # removing the file using the os.remove() method
            os.remove(file_path)
        else:
            # file not found message
            print("File not found in the directory")

    from shutil import copyfile
    src = '/aul/homes/qli027/projects/disaggregation/final_version/prepare_for_figures/noise/UNSW/' + str(house_num) + '/'
    for i in range(1,23):
        copyfile(src +'channel_' + str(i) + '.dat' , input_path+'channel_' + str(i) + '.dat')


    path = '/aul/homes/qli027/projects/disaggregation/final_version/prepare_for_figures/noise/UNSW/'
  

    convert_redd('/aul/homes/qli027/projects/disaggregation/final_version/data/N_houses/low_freq/', path + '/redd.h5')