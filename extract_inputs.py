# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 23:38:51 2021

@author: Sree
"""
import json


def fetch_json_file_data(filename):
    json_data = {}
    with open(filename,'r') as json_file:
        json_data=json.load(json_file)
        
    return json_data

def fetch_input_file_data(filename):
    input_data = []
    with open('input_file.txt', "r") as input_file:
        input_data = input_file.read().split('\n')
        
    return input_data

def convert_array_to_dict(data_list, key_name, value_name):
    converted_dict = {d[key_name].upper():d[value_name] for d in data_list}        
    return converted_dict