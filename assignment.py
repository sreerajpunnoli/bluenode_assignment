# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 00:56:21 2021

@author: Sree
"""

#%%
import json


CSV_KEYS = 'Section,Sub-Section,Given DataType,Expected DataType,Given Length,Expected MaxLength,Error Code'.split(',')

#%%
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
    converted_dict = {d[key_name]:d[value_name] for d in data_list}        
    return converted_dict


def get_data_type(row_array, index):    
    data_type = 'digit' if row_array[index].isnumeric() else 'word_characters'
    return data_type


def get_given_lenth(row_array, index):
    return len(row_array[index])


def get_error_code(expected_data_type, given_data_type, expected_max_length, given_length):
    if expected_data_type == given_data_type:
        return 'E01' if expected_max_length >= given_length else 'E03'
    else:
        return 'E02' if expected_max_length >= given_length else 'E04'
    
#%%
    
    
# Section,Sub-Section,Given DataType,Expected DataType,Given Length,Expected MaxLength,Error Code
#import csv
#with open(..., 'w', newline='') as myfile:
#     wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
#     wr.writerow(mylist)
        
input_data = fetch_input_file_data('input_file.txt')
error_codes = fetch_json_file_data('error_codes.json')
standard_definition = fetch_json_file_data('standard_definition.json')

error_code_dict = convert_array_to_dict(error_codes, 'code', 'message_template')
standard_definition_dict = convert_array_to_dict(standard_definition, 'key', 'sub_sections')


converted_report_list = []
summary = ''
for row in input_data:
    row_array = row.split('&')
    if not row_array:
        continue
    
    row_array_length = len(row_array)
    
    section = row_array[0]
    index = 0
    for sub_section_dict in standard_definition_dict[section]:
        index += 1
        sub_section = sub_section_dict['key']
        expected_data_type = sub_section_dict['data_type']
        expected_max_length = sub_section_dict['max_length']
        
        if len(row_array) <= index:
            given_data_type = ''
            given_length = ''
            error_code = 'E05'
        else:
            given_data_type = get_data_type(row_array, index)
            given_length = get_given_lenth(row_array, index)
            error_code = get_error_code(expected_data_type, given_data_type, expected_max_length, given_length)
        
        row = [section, sub_section, given_data_type, expected_data_type, given_length, expected_max_length, error_code]
        converted_report_list.append(row)
        
        row_summary = error_code_dict[error_code].replace('LXY', sub_section) \
                        .replace('LX', section).replace('{data_type}', expected_data_type) \
                        .replace('{max_length}', str(expected_max_length))
        summary += row_summary
        
    summary += '\n'

#
# Write to csv
# Write summary txt file

