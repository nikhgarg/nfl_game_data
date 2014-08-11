# -*- coding: utf-8 -*-
"""
Created on Thu May 15 13:34:07 2014

@author: Nikhil
"""

class Game:
    tag = ''
    data = {}
    def __init__(self, tag, data={}):
        self.data = data
        self.tag = tag
    def __str__( self ):
        return self.tag + "\t" + str(self.data)
#    Stadium = ''
#    StartTime = ''
#    Surface = ''
#    Duration = 0
#    Attedance = ''
#    Weather = ''
#    VegasLine = ''
#    Winner = ''
#    Loser = ''
#    PtsW = 0
#    PtsL = 0
#    YdsW= 0
#    TOW = 0
#    TOL = 0
#    YdsL = 0

team_dict = {
    'Denver Broncos': 'den',
    'Detroit Lions': 'det',
    'Jacksonville Jaguars': 'jax',
    'Indianapolis Colts': 'clt',
    'St. Louis Rams': 'ram',
    'Los Angeles Rams' : 'ram',
    'Cleveland Browns': 'cle',
    'New Orleans Saints': 'nor',
    'Pittsburgh Steelers': 'pit',
    'Chicago Bears': 'chi',
    'San Francisco 49ers': 'sfo',
    'Tennessee Titans': 'oti',
    'Tennessee Oilers': 'oti',    
    'New York Giants': 'nyg',
    'New York Jets': 'nyj',
    'Green Bay Packers': 'gnb',
    'Houston Oilers': 'oti',
    'Houston Texans': 'htx',
    'Minnesota Vikings': 'min',
    'Dallas Cowboys': 'dal',
    'Miami Dolphins': 'mia',
    'Atlanta Falcons': 'atl',
    'Seattle Seahawks': 'sea',
    'Carolina Panthers': 'car',
    'Washington Redskins': 'was',
    'Philadelphia Eagles': 'phi',
    'New England Patriots': 'nwe',
    'San Diego Chargers': 'sdg',
    'Buffalo Bills': 'buf',
    'Arizona Cardinals': 'crd',
    'Phoenix Cardinals': 'crd',
    'Cincinnati Bengals': 'cin',
    'Baltimore Ravens': 'rav',
    'Tampa Bay Buccaneers': 'tam',
    'Oakland Raiders': 'rai',
    'Los Angeles Raiders' : 'rai',
    'Kansas City Chiefs': 'kan'
    }
    
months_dict = {
    'Jan': '01',
    'Feb': '02',
    'Mar': '03',
    'Sep': '09',
    'Oct': '10',
    'Nov': '11',
    'Dec': '12',
    'Aug': '08'
    }