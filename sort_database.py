# This is a script with the functions required to post process and sort the data into a cleaner database
from os import listdir
from os.path import isfile, join
import glob
import csv
import json
import numpy as np
import pandas as pd
from data_download import *
from my_secrets import get_account_name
import re

def get_json_file(path):
    list_of_files = get_list_of_files(path)
    # taking one of the files as a test to extract information
    main_file = path + list_of_files[2] + '.json' 
    path_to_processed_database = '/Users/kevin/Documents/Kevin/Projects/my_league_stats/Data/processed_data/'
    #print(main_file)
    f = open(main_file)
    data = json.load(f)
    my_data = data['participants']
    my_account = detect_account_in_json(my_data)
    print(my_account)
    sub_folder = my_account.replace(' ', '') + '/match_data.csv'
    total_path = path_to_processed_database + sub_folder
    print(total_path)
    for idx, var in enumerate(my_data):
        if var['summonerName'] == my_account:
            #print(var)   
            # This next line gets the dictionary in a way so that when converting to a pandas dataframe the dict keys are used as column headings
            #df = pd.DataFrame.from_dict(var) 
            var = {k: [v] for k,v in var.items()}
            df = pd.DataFrame.from_dict(var)
            df.to_csv(total_path, mode='a', index='False', header='False')
            print(f"data was written for {my_account}!")

def detect_account_in_json(data):
    account_list = get_account_name();
    print(account_list)
    for idx, var in enumerate(data):
        if var['summonerName'] in account_list:
            return var['summonerName']

get_json_file('/Users/kevin/Documents/Kevin/Projects/my_league_stats/Data/match_data/')
