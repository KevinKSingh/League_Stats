#from data_download import *
import data_download
from my_secrets import get_api_key, get_account_name
from riotwatcher import LolWatcher, ApiError
# This is a comment to see if github from terminal works
# Getting secrets infor like API Key and account name
riot_api_key = get_api_key()
watcher = LolWatcher(riot_api_key)
region = 'euw1'
if __name__ == '__main__':
    account_list = get_account_name()
    for account in account_list:
        print(f"Account being processed: {account}")
        data = data_download.get_account_information(watcher, region, account)
        matches = data_download.get_match_list(watcher, region, data)
        #get_match_data(watcher, region, match_id)
        x = data_download.get_match_list_from_database('/Users/kevin/Documents/Kevin/Projects/my_league_stats/Data/match_database/match_database.csv')
        match_list = data_download.build_match_database(watcher, region, data)
        data_download.get_match_data(watcher, region)
    print(f"There are {len(x)} games in the database!")
