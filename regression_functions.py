# -*- coding: utf-8 -*-
"""
Created on Thu May 15 19:24:00 2014

@author: Nikhil
"""

def win_score(game):
    return game.data["PtsW"]
def loss_score(game):
    return game.data["PtsL"]
def total_score(game):
    if (game.data["PtsW"] is not None) and (game.data["PtsL"] is not None):
        return game.data["PtsW"] + game.data["PtsL"]
    else:
        return None

def win_yards(game):
    return game.data["YdsW"]
def loss_yards(game):
    return game.data["YdsL"]
def total_yards(game):
    if (game.data["YdsW"] is not None) and (game.data["YdsL"] is not None):
        return game.data["YdsW"] + game.data["YdsL"]
    else:
        return None
        
def win_turnovers(game):
    return game.data["TOW"]
def loss_turnovers(game):
    return game.data["TOL"]
def total_turnovers(game):
    if (game.data["TOW"] is not None) and (game.data["TOL"] is not None):
        return game.data["TOW"] + game.data["TOL"]
    else:
        return None
def over_under(game):
    return game.data["Over/Under"]

def difference_over_under(game):
    if (game.data["Over/Under"] is not None) and (total_score(game) is not None):
        return total_score(game) - game.data["Over/Under"]
    else:
        return None
       
def temperature(game):
    return game.data["temperature"]
    