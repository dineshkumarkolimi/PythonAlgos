#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Jul 04 2023

@author: dineshkumarkolimi

Given a string str, find the length of the longest substring without repeating characters. 

Example:

Example 1:
Input: “ABCDEFGABEF”
Output: 7
Explanation: The longest substring without repeating characters are “ABCDEFG”, “BCDEFGA”, and “CDEFGAB” with lengths of 7

Example 2:
Input: “GEEKSFORGEEKS”
Output: 7
Explanation: The longest substrings without repeating characters are “EKSFORG” and “KSFORGE”, with lengths of 7
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
