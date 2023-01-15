# League Stats Application

This repository is contains the code to fetch the data from the Riot Games API and create a big database. The aim here is to pull all the information so that it can be presented similar to what is found in www.cricinfo.com. I like using sites like op.gg and league of graphs but was usually annoyed to find that my normal games were only temporarily stored or needed to be extrapulated. Similar to rewind.lol I would like to build  a database where I can get champion specific stats for the different queues (ranked, normal, ARAM, flex) as well as the cumulative sum (potentially even rift vs aram). 

Finally I would like to create a front end display for this as well in Typescript or something else where the data can be visualized in a nice easy to use manner. But development for this has yet to begin, I am still trying to figure out what all is needed on the back-end side.

## Current Progress

1. can contact the Riot API and download 20 of the lastest games for the game ID
2. can append to the newest games to a global list of database of game IDs
3. can download the match specific data for each game and store in JSON
4. added functionality to detect which gameIDs have been processed already by checking which JSON files exist in the folder
5. Subtract the list of match ids which have already been processed from the ones which need to be processed 
6. Separate account functionality, the main.py script loops over all the accounts listed in the get_account function
7. Post Processing file can detect which of my accounts are in the game and sort those into the appropriate processed data folder

## Features To Add

1. Decide what details from the JSON files we want to store and how (IN PROGRESS)
2. Create a script to parse the data from the match JSON files to store champion specific information per account (IN PROGRESS)
3. Add functionality which detects which of the games have already been processed from the overall match_database and which still require processing so that there is no work which is repeated unnecessarily.


## How To Run this code

1. add your Riot API get to the my_secrets.py file , delete the 0 and enter the API key as a string
2. add your accounts to the list in the my_secrets.py file
3. in the main.py file, change the region to the appropriate region your account is located in
4. run main.py

## Future Development

1. Front end code
