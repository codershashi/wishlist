#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 17:02:58 2023

@author: shashi
"""

import csv
import requests

file_path = 'Task 2 - Intern.csv'

with open(file_path, 'r', newline='') as csvfile:
    reader = csv.reader(csvfile)
    next(reader, None)
    for urls in reader:
        url = urls[0]
        try:
            response = requests.head(url)
            print(f'({response.status_code}) {url}') 
        except (requests.ConnectionError, requests.Timeout, requests.RequestException) as e:
            print (f'(Error: {e}), {url}')
      