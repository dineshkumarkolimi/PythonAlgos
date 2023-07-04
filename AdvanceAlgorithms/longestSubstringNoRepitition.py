#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Jul 04 2023

@author: dineshkumarkolimi

Program: longest non repeating char substring
"""
"""
    Finds the longest non repeating char substring in a string
    
    Parameters
    ----------
    str : str
        The string to find the longest non repeating char substring in
    
    Returns
    -------
    int
        length of longest non repeating char substring in the string
"""
def longest_substring_no_repeat(string):
    alphabets = {}
    pos = -1
    max_len = 0
    
    for index, letter in enumerate(string):
        if letter in alphabets and alphabets[letter] > pos:
            pos = alphabets[letter]
        alphabets[letter] = index
        max_len = max(max_len, index - pos)
        
    return max_len
        
if __name__ == '__main__':
    string = 'bbbbbb'
    print(longest_substring_no_repeat(string))