# -*- coding: utf-8 -*-
"""
Created on Thu May 15 16:55:47 2014

@author: Nikhil
"""

from GameClass import Game
from load_tagged_data import load_data
from GameClass import team_dict
from scipy import stats
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import pylab

def record(data, team_name):
    team_games = []

    for game in data:
        if (game.data["Home Team"] == team_name or game.data["Away Team"] == team_name):
            team_games.append(game)
      
    won = 0
    lost = 0
    tied = 0
    
    for game in team_games:
        if (game.data["PtsW"] == game.data["PtsL"]):
            tied+=1
        elif (game.data["Winner"] == team_name): #is winning team, not tied
            won+=1
        else:
            lost+=1
    #print str(won)+"-"+str(lost)+"-"+str(tied)
    return [won, lost, tied]
    
def regress_functions(data, fun1, fun2):
    x = []
    y = []
    for game in data:
        val1 = fun1(game)
        val2 = fun2(game)
        if (val1 is not None and val2 is not None):
            x.append(int(fun1(game)))
            y.append(int(fun2(game)))
    slope, intercept, r_value, p_value, std_err = stats.linregress(x,y)
#    min_x = min(x)
#    max_x = max(x)
#    delta = 1
#    x_range = range(min_x, max_x, delta)
#    y_range = [slope*xx + intercept for xx in x_range]
#    
#    string1 = fun1.__name__ 
#    string2 = fun2.__name__
#    title = string1 + " vs. " + string2
#    plt.scatter(x,y)
#    plt.plot(x_range, y_range)
#    plt.xlabel(string1)
#    plt.ylabel(string2)
#    plt.title(title)
#    pylab.savefig(title+".jpg", bbox_inches='tight')
#    plt.close()
    
    return r_value
    