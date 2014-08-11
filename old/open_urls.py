# -*- coding: utf-8 -*-
"""
Created on Wed May 14 12:01:34 2014

@author: Nikhil
"""

urlbegin = "http://www.pro-football-reference.com/years/"
urlend = "/games.htm"

for i in xrange(1960, 2014):
    print (urlbegin + str(i) + urlend)