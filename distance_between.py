# -*- coding: utf-8 -*-
"""
Function. 

This function works for any arbitrary pair of agents. 
The function recieves as input; two arbitary agents (two rows in the agents list, each containing two values), 
and calculates how far apart they are.

@author: Baba Gana Modu
"""
#Function defination
def distance_between(agents_row_a, agents_row_b):
    #Function distance calculation formular 
    return (((agents_row_a[0] - agents_row_b[0])**2) + ((agents_row_a[1] - agents_row_b[1])**2))**0.5