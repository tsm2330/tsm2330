# -*- coding: utf-8 -*-
"""
Created on Tue Aug 23 09:22:53 2022

@author: user
"""

def twosum (a,b):
    list=[]
    for i in range(len(a)):
        for j in range(a+1,len(a)):
            if a[i]+a[j]==b:
                list.append((i,j))
    return list             
            
        
    