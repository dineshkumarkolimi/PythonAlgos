#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  9 14:01:32 2022

@author: dineshkumarkolimi

program: extracting from url
"""

from urllib.request import urlopen
import json

if __name__ == "__main__":
    url = "https://www.geeksforgeeks.org/how-to-read-a-json-response-from-a-link-in-python/"
    response = urlopen(url)
    print(response)
    myJson = json.load(response.read())
    print(myJson)

