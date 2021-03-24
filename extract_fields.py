# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 23:21:19 2021

@author: Sree
"""
import re


def get_missing_default_fields():
    given_data_type = ''
    given_length = ''
    error_code = 'E05'
    
    return given_data_type, given_length, error_code


def get_empty_default_fields():
    given_data_type = ''
    given_length = ''
    error_code = 'E04'
    
    return given_data_type, given_length, error_code
    

def get_data_type(row_array, index):
    if bool(re.match("^[0-9]*$", row_array[index])):
        return 'digits'
    elif bool(re.match("^[A-Za-z]*$", row_array[index])):
        return 'word_characters'
    else:
        return 'other'


def get_given_lenth(row_array, index):
    return len(row_array[index])


def get_error_code(expected_data_type, given_data_type, expected_max_length, given_length):
    if expected_data_type == given_data_type:
        return 'E01' if expected_max_length >= given_length else 'E03'
    else:
        return 'E02' if expected_max_length >= given_length else 'E04'