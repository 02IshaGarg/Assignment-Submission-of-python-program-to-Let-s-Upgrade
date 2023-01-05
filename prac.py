# -*- coding: utf-8 -*-
"""
Created on Thu Jan  5 20:55:36 2023

@author: Lefty Ishu
"""

# Write a program to construct the following pattern, using a nested for loop.
# * 
# * * 
# * * * 
# * * * * 
# * * * * * 
# * * * * 
# * * * 
# * * 
# *

rows = 5
for row in range(1, rows+1):
        print("* " * row)
for row in range(rows-1, 0, -1):
        print("* " * row)


















