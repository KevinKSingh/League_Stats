from riotwatcher import LolWatcher, ApiError
from my_secrets import get_api_key

def get_mastery_points(api_key, region, summoner_name, champion_id):
    # Initialize the LolWatcher with your API key
    watcher = LolWatcher(api_key)
    try:
        # Get summoner information
        summoner = watcher.summoner.by_name(region, summoner_name)
        # Get mastery information for the given champion
        champion_mastery = watcher.champion_mastery.by_summoner(region, summoner["id"])
        for mastery in champion_mastery:
            if mastery["championId"] == champion_id:
                return mastery["championPoints"]
        return 0  # If no mastery found for the champion
    except ApiError as e:
        print(f"Error: {e.response.status_code} - {e.response.text}")
        return None

# Replace with your Riot API key
riot_api_key = get_api_key()

# Replace with the region, summoner name, and champion ID you want to use
region = "euw1"
summoner_name = []
# This is the champion ID for Yasuo
champion_id = 157
total = 0
for summoner in summoner_name:
    mastery_points = get_mastery_points(riot_api_key, region, summoner, champion_id)
    if mastery_points is not None:
        total += mastery_points 
print(f"The total mastery points for Yasuo are: {total}")

