# -*- coding: utf-8 -*-
"""
Created on Sat Sep 22 00:33:38 2018

@author: Jason Tran
"""

def weight_on_planets():
    """
    Reads input (user weight on Earth) and prints corresponding weights on Mars and Jupiter.
    """
    # write your code here
    earthWeight = int(input())
    print('What do you weigh on earth? \nOn Mars you would weigh ' + str(earthWeight*.38) + ' pounds.\nOn Jupiter you would weigh ' + str(earthWeight*2.34) + ' pounds.')
   
if __name__ == '__main__':
    weight_on_planets()