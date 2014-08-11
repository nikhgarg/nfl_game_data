# -*- coding: utf-8 -*-
"""
Created on Thu May 15 12:04:05 2014

@author: Nikhil
"""
import csv
    
from GameClass import team_dict
from GameClass import months_dict
print team_dict
count = 0
year = -1

with open('tagged_nfl_game_results.csv', 'w') as csvoutput:
    writer = csv.writer(csvoutput, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL, lineterminator='\n')
    with open('nfl_game_results.csv', 'rb') as csvfile:
         reader = csv.reader(csvfile, delimiter=',', quotechar='|')
         for row in reader:
             if (len(row)>0):
                 count = count+1
                 if "year" in row[0]:
                     year = row[0][-4:]
                 if (year is 1960):
                     continue
                 if row[0].isdigit(): #start of a game row, non-playoffs
                     date = row[2].split("-")
                     day = ('0' + date[0])[-2:]
                     month = months_dict[date[1]]
    
                     tag = str(year)+str(month)+str(day) + "0"
                     if ('@' in row[5]):
                         tag = tag + team_dict[row[6]]
                     else:
                         tag = tag + team_dict[row[4]]
                     writer.writerow(['Winner', row[4] , tag])
                     writer.writerow(['Loser', row[6] , tag])
                     writer.writerow(['PtsW', row[7] , tag])
                     writer.writerow(['PtsL', row[8] , tag])
                     writer.writerow(['YdsW', row[9] , tag])
                     writer.writerow(['TOW', row[10] , tag])
                     writer.writerow(['YdsL', row[11] , tag])
                     writer.writerow(['TOL', row[12] , tag])                    
print count