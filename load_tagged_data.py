# -*- coding: utf-8 -*-
"""
Created on Thu May 15 13:27:50 2014

@author: Nikhil
"""


from GameClass import Game
import csv


def load_data( filename = "tagged_nfl_game_rows.csv"):

    all_data = []
    
    with open(filename, 'rb') as csvfile:
         reader = csv.DictReader(csvfile, delimiter=',', quotechar='|')
         for row in reader:
             for i in row.keys():
                 if len(row[i])==0:
                     row[i]=None
                 elif(row[i].isdigit()):
                     row[i] = int(row[i])
                 elif(i=="Over/Under"):
                     row[i] = float(row[i][0:4])
             temp = Game(row["tag"], row)
             all_data.append(temp)
    return all_data
