# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 17:54:38 2020

@author: omarm

Question:
-------------
Given a string in the form 'AAAABBBBCCCCCDDEEEE' compress it to become 'A4B4C5D2E4'. For this problem, you can falsely "compress" strings of single or double letters. For instance, it is okay for 'AAB' to return 'A2B1' even though this technically takes more space.
The function should also be case sensitive, so that a string 'AAAaaa' returns 'A3a3'.

"""

#333343121
s = "AAABCCDDDDDzzzzllx"

def str_comp(s):
    
    n = len(s) # The length.
    
    #base case
    if n == 0:
        return ''
    
    # String to be printed.
    prt = ""
    
    # iterator
    i = 0
    
    while i < n-1:
        if s[i] == s[i+1]:
            sm = 0
            while i < n-1 and s[i] == s[i+1]:
                sm += 1
                i += 1
            sm += 1
            print(s[i],sm)
            prt += str(s[i])+str(sm)
            
        else:
            print(s[i],1)
            prt += str(s[i])+'1'
        i += 1
        print('index:',i)
    # Checking if the last element is a loner.
    if s[n-1] != s[n-2]:
        print(s[i],1)
        prt += str(s[i])+'1'
        
    return prt
            
