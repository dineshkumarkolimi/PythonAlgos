#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  9 14:01:32 2022

@author: dineshkumarkolimi

program: extracting from url
"""

from urllib.request import urlopen
import json
import requests

#best alternative for executing get method
def get_method(ur):
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return None

if __name__ == "__main__":
    url = "https://www.geeksforgeeks.org/how-to-read-a-json-response-from-a-link-in-python/"
    response = urlopen(url)
    print(response)
    myJson = json.load(response.read())
    print(myJson)
    print(get_method(url))

