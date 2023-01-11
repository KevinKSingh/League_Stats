# League Stats Application

This repository is contains the code to fetch the data from the Riot Games API and create a big database. The aim here is to pull all the information so that it can be presented similar to what is found in www.cricinfo.com. I like using sites like op.gg and league of graphs but was usually annoyed to find that my normal games were only temporarily stored or needed to be extrapulated. Similar to rewind.lol I would like to build  a database where I can get champion specific stats for the different queues (ranked, normal, ARAM, flex) as well as the cumulative sum (potentially even rift vs aram). 

Finally I would like to create a front end display for this as well in Typescript or something else where the data can be visualized in a nice easy to use manner. But development for this has yet to begin, I am still trying to figure out what all is needed on the back-end side.

## Current Progress

1. can contact the Riot API and download 20 of the lastest games for the game ID
2. can append to the newest games to a global list of database of game IDs
3. can download the match specific data for each game and store in JSON
4. added functionality to detect which gameIDs have been processed already by checking which JSON files exist in the folder

## Features To Add

1. Subtract the list of match ids which have already been processed from the ones which need to be processed
2. Create a script to parse the data from the match JSON files to store champion specific information
3. Add Separate account functionality
  - i.e. I want my main account data to be separate from smurf accounts
  - read accounts in from a list to be processed eg my_accounts = ['acc_1', 'acc_2] then func_do_everthing(my_accounts) 


## Future Development

1. Front end code
