#from data_download import *
import data_download
from my_secrets import get_api_key, get_account_name
from riotwatcher import LolWatcher, ApiError
from menu import get_user_input
# This is a comment to see if github from terminal works
# Getting secrets infor like API Key and account name
riot_api_key = get_api_key()
watcher = LolWatcher(riot_api_key)
if __name__ == '__main__':
    data_dict = get_user_input()
    region = list(data_dict.keys())[0]  
    account_list = data_dict[region]
    for account in account_list:
        print(f"Account being processed: {account}")
        data = data_download.get_account_information(watcher, region, account)
        matches = data_download.get_match_list(watcher, region, data)
        #get_match_data(watcher, region, match_id)
        x = data_download.get_match_list_from_database('/Users/kevin/Documents/Kevin/Projects/my_league_stats/Data/match_database/match_database.csv')
        match_list = data_download.build_match_database(watcher, region, data)
        data_download.get_match_data(watcher, region)
    print(f"There are {len(x)} games in the database!")
