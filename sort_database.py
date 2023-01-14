# This is a script with the functions required to post process and sort the data into a cleaner database
from os import listdir
from os.path import isfile, join
import glob
import csv
import json
import numpy as np
import pandas as pd
from data_download import *

def get_json_file(path, account_name):
    list_of_files = get_list_of_files(path)
    # taking one of the files as a test to extract information
    main_file = path + list_of_files[0] + '.json' 
    path_to_processed_database = '/Users/kevin/Documents/Kevin/Projects/my_league_stats/Data/processed_data/'
    sub_folder = account_name.replace(' ', '') + '/match_data.csv'
    total_path = path_to_processed_database + sub_folder
    print(total_path)
    #print(main_file)
    f = open(main_file)
    data = json.load(f)
    my_data = data['participants']
    for idx, var in enumerate(my_data):
        if var['summonerName'] == account_name:
            #print(var)   
            # This next line gets the dictionary in a way so that when converting to a pandas dataframe the dict keys are used as column headings
            var = {k: [v] for k,v in var.items()}
            df = pd.DataFrame.from_dict(var) 
            df.to_csv(total_path)
get_json_file('/Users/kevin/Documents/Kevin/Projects/my_league_stats/Data/match_data/', 'singhasong ')
