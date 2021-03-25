# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 23:38:51 2021

@author: Sree
"""
import json


class ExtractInputFiles:
    
    def fetch_json_file_data(self, filename):
        ''' Fetch json file data and return it as dictionary '''
        json_data = {}
        with open(filename,'r') as json_file:
            json_data=json.load(json_file)
            
        return json_data
    
    def fetch_input_file_data(self, filename):
        ''' Fetch input file data and return it as a list '''
        input_data = []
        with open(filename, "r") as input_file:
            input_data = input_file.read().split('\n')
            
        return input_data
    
    def convert_list_to_dict(self, data_list, key_name, value_name):
        ''' Convert list to dictionary using the key and value keys given '''
        converted_dict = {d[key_name].upper():d[value_name] for d in data_list}        
        return converted_dict
    

# Singleton Object
extract_input_files_obj = ExtractInputFiles()