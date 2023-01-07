#This code is to run an application which fetches data from the RIOT Games API and stores them for my games
from riotwatcher import LolWatcher, ApiError
import pandas as pd
from my_secrets import get_api_key, get_account_name

# global variables

# Getting the Riot API KEY
riot_api_key = get_api_key()   
watcher = LolWatcher(riot_api_key)

# Setting Region and fetching my account names
my_region = 'euw1' 
account_list = get_account_name()
account_name = account_list[0]

# This prints information on the account 
me = watcher.summoner.by_name(my_region, account_name)


# Returning the ranked stats for my account

my_ranked_stats = watcher.league.by_summoner(my_region, me['id'])
print(my_ranked_stats)

# Access Match Data 
my_matches = watcher.match.matchlist_by_puuid(my_region, me['puuid'])
print(my_matches)
print(len(my_matches))

# Accessing data from the last match

# my_matches is a list of the last 20 games where each entry is an Game ID 
last_match = my_matches[0]

match_detail = watcher.match.by_id(my_region, last_match) 

#print(match_detail.keys())

#print(match_detail['info'].keys())
#print("info keys")

#print(match_detail['metadata'].keys())

var = match_detail['info']['participants'] 



# Doing some data exploration to see what is stored in the data
# This for loop currently outputs all of the summoner names and the champions that they played in that game
for row in var:
    print(f"Summoner Name: {row['summonerName']}, Champion Played: {row['championName']}")
    #for idx, value in enumerate(row):
    #    print(f"Key: {value}, Value: {var[0][value]}")
    #print('\n')
    
participants = []
for row in var:
    participants_row = {}
    participants_row['champion'] = row['championId'] 
    #participants_row['spell1'] = row['spell1Id']
    participants.append(participants_row)


#print(participants)

# Accessing Data Dragon, now we have only some information from the game but from Data Dragon we can get all of the static information for League of Legends

# check league's latest version

latest = watcher.data_dragon.versions_for_region(my_region)['n']['champion']
print(latest)
# lets get some champions static information
# This returns a dictionary of all the champions including detailed information on their stats and descriptions
static_champ_list = watcher.data_dragon.champions(latest, False, 'en_US')
champ_dict = {}
for key in static_champ_list['data']:
    row = static_champ_list['data'][key]
    champ_dict[row['key']] = row['id']

#df = pd.DataFrame(participants)
#print(df)
print(champ_dict)

# You can extract the postition which was played in the game by using a map to identify each champion's position
# (MID_LANE, SOLO): MIDDLE
# (TOP_LANE, SOLO): TOP
# (JUNGLE, NONE): JUNGLE
# (BOT_LANE, DUO_CARRY): BOTTOM
# (BOT_LANE, DUO_SUPPORT): UTILITY




