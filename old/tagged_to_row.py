# -*- coding: utf-8 -*-
"""
Created on Thu May 15 13:50:20 2014

@author: Nikhil
"""

from GameClass import team_dict

#load data into dictionary with keys tags, values - another dictionary
    #this value dictionary has the stuff

import csv

all_data = {}
duplicate = 0

with open('tagged_nfl_game_rows.csv', 'w') as csvoutput:
    writer = csv.DictWriter(csvoutput, fieldnames=['tag', 'Year', 'Month', 'Day', 'Home Team', 'Away Team', 'Winner', 'Loser', 'PtsW', 'PtsL', 'YdsW', 'YdsL', 'TOW', 'TOL', 'Start Time', 'Stadium', 'Attendance', 'Surface', 'temperature', 'humidity', 'wind', 'Over/Under', 'Vegas Line', 'Duration', 'Super Bowl MVP'], delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL, lineterminator='\n')
    with open('total_tagged_nfl_game_metadata_since_1993.csv', 'rb') as csvfile:
         reader = csv.reader(csvfile, delimiter=',', quotechar='|')
         for row in reader:
             if row[-1] not in all_data:
                 all_data[row[-1]] = {row[0]:row[1]}
             else:
                 exist = all_data[row[-1]]
                 
                 if (row[0] in exist):
                     duplicate = duplicate + 1                 
                 
                 if row[0] == "Attendance":
                     exist["Attendance"] = str(row[1][1:]) + str(row[2][:-1])
                 elif row[0] == "Weather":
                     degrees = (row[1])[1:-8]
                     exist["temperature"] = degrees
                     if ("relative" in row[2]):
                         relativeHumidity = row[2][-3:-1]
                         wind = row[3][5:-4]
                         exist["humidity"] = relativeHumidity
                     else:
                         wind = row[2][5:-4]
                     exist["wind"] = wind
                 else:
                     exist[row[0]] = row[1]
                 all_data[row[-1]] = exist
    writer.writeheader()#['tag', 'Winner', 'Loser', 'PtsW', 'PtsL', 'YdsW', 'YdsL', 'TOW', 'TOL', 'Start Time', 'Stadium', 'Attendance', 'Surface', 'temperature', 'humidity', 'wind', 'Over/Under', 'Vegas Line', 'Duration', 'Super Bowl MVP'])

    k = sorted(all_data.keys())
    
    for a in k:
        team_tag = a[-3:]
        game_data = all_data[a]
        game_data['Year'] = a[0:4]
        game_data['Month'] = a[4:6]
        game_data['Day'] = a[6:8]
        if ("Winner" in game_data):
            if (team_dict[game_data["Winner"]]==team_tag):
                game_data["Home Team"] = game_data["Winner"]
                game_data["Away Team"] = game_data["Loser"]
            else:
                game_data["Home Team"] = game_data["Loser"]
                game_data["Away Team"] = game_data["Winner"]
        game_data["tag"] = a
        writer.writerow(game_data)