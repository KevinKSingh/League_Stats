from data_download import *
from my_secrets import get_api_key, get_account_name
from riotwatcher import LolWatcher, ApiError
# This is a comment to see if github from terminal works
# Getting secrets infor like API Key and account name
riot_api_key = get_api_key()
watcher = LolWatcher(riot_api_key)
region = 'euw1'
account_list = get_account_name()
account_name = account_list[0]
print(account_name)
if __name__ == '__main__':
    data = get_account_information(watcher, region, account_name)
    matches = get_match_list(watcher, region, data)
    match_id = matches[0]
    #get_match_data(watcher, region, match_id)
    x = get_match_list_from_database('/Users/kevin/Documents/Kevin/Projects/my_league_stats/Data/match_database/match_database.csv')
    match_list = build_match_database(watcher, region, data)
    print(f"The Number of Matches played so far are: {len(match_list)}")
    get_match_data(watcher, region)
    
