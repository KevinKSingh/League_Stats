This Repository is some code to fetch data from the Riot Games API and create a big database similar to the layout
for the individual player statistics as found on www.cricinfo.com. The aim of this is to get granular and top level numbers for any League of Legends player. This was partially inspired by the rewind.lol website. 

For example, if I wanted to know (and had built the database of games appropriately) I would be able to take one years worth of League match data and break it down to see my champion performances in Normal games vs Ranked games. Maybe find one particular champion I really struggle against. 


-> CURRENT PROGRESS

-> can contact the API and download 20 of the latest game IDs
-> can append the newest to a global database of game IDs

-> FEATURES TO ADD

-> For each match_id pull down the metadata and match specific information
-> store that in JSON or some other appropriate file format
-> Create functions to build queries from the match_detail_database to create the overarching stats

