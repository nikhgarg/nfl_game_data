# -*- coding: utf-8 -*-
"""
Created on Thu May 15 18:44:22 2014

@author: Nikhil
"""

from calculate_statistics import record
from calculate_statistics import regress_functions
from regression_functions import *

from GameClass import Game
from load_tagged_data import load_data
from GameClass import team_dict

data = load_data() #list of Game objects
    
#total_wins = 0
#total_losses = 0
#total_ties= 0
#total_rec = [0,0,0]
#for team_name in team_dict.keys():
#    rec = record(data, team_name)
#    total_wins += rec[0]
#    total_losses += rec[1]
#    total_ties += rec[2]
#    total_rec = [i+j for i,j in zip(total_rec, rec)]
#    print team_name + "\t\t" + str(rec)
#print total_rec

    
#fun1 = difference_over_under
#fun2 = over_under   
#regress_functions(data, fun1, fun2)

def run_all_regress_functions(data):
    functions = [win_score, loss_score, total_score, win_yards, loss_yards, total_yards, win_turnovers, loss_turnovers, total_turnovers, over_under, difference_over_under, temperature]
    count = 0
    r_results = []
    names = []
    for fun1ind in xrange(0,len(functions)):
        for fun2ind in xrange(fun1ind+1, len(functions)):
            fun1 = functions[fun1ind]
            fun2 = functions[fun2ind]
            rvalue = pow(regress_functions(data, fun1, fun2),2)
            r_results.append(rvalue)
            
            string1 = fun1.__name__ 
            string2 = fun2.__name__
            title = string1 + " vs. " + string2
            names.append(title)
            
            count+=1
            print count, rvalue
    indices = reversed([i[0] for i in sorted(enumerate(r_results), key=lambda x:x[1])])
    for index in indices:
        print "%s\t\t\t%f" % (names[index], r_results[index])

run_all_regress_functions(data)