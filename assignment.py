# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 00:56:21 2021

@author: Sree
"""

#%%
import extract_fields
import extract_inputs
import write_results
import os

CSV_REPORT_COLUMN_NAMES = 'Section,Sub-Section,Given DataType,Expected DataType,'\
                            'Given Length,Expected MaxLength,Error Code'.split(',')

INPUT_DIRECTORY = 'inputs'
RESULTS_DIRECTORY = 'results'

INPUT_FILE = os.path.join(INPUT_DIRECTORY, 'input_file.txt')
ERROR_CODE_FILE = os.path.join(INPUT_DIRECTORY, 'error_codes.json')
STANDARD_DEFINITION_FILE = os.path.join(INPUT_DIRECTORY, 'standard_definition.json')
REPORT_FILENAME = os.path.join(RESULTS_DIRECTORY, 'report.csv')
SUMMARY_FILENAME = os.path.join(RESULTS_DIRECTORY, 'summary.txt')


ERROR_CODE_KEY_NAME = 'code'
ERROR_CODE_VALUE_NAME = 'message_template'
STANDARD_DEFINITION_KEY_NAME = 'key'
STANDARD_DEFINITION_VALUE_NAME = 'sub_sections'


def parse_input(input_data, error_code_dict, standard_definition_dict):
    converted_report_list = []
    summary = ''
    
    for row in input_data:
        row_array = row.split('&')
        if not row_array:
            continue
        
        section = row_array[0].upper()
        
        index = 0
        for sub_section_dict in standard_definition_dict[section]:
            index += 1
            sub_section = sub_section_dict['key'].upper()
            expected_data_type = sub_section_dict['data_type']
            expected_max_length = sub_section_dict['max_length']
            
            if index >= len(row_array):
                given_data_type, given_length, error_code = extract_fields.get_missing_default_fields()
            elif row_array[index] == '':
                given_data_type, given_length, error_code = extract_fields.get_empty_default_fields()
            else:
                given_data_type = extract_fields.get_data_type(row_array, index)
                given_length = extract_fields.get_given_lenth(row_array, index)
                error_code = extract_fields.get_error_code(expected_data_type, given_data_type, expected_max_length, given_length)
            
            row = [section, sub_section, given_data_type, expected_data_type, given_length, expected_max_length, error_code]
            converted_report_list.append(row)
            
            row_summary = error_code_dict[error_code].replace('LXY', sub_section) \
                            .replace('LX', section).replace('{data_type}', expected_data_type) \
                            .replace('{max_length}', str(expected_max_length))
            summary += row_summary + '\n'
            
        summary += '\n'
        
    return converted_report_list, summary

    
def parse_bluenode_data():
    input_data = extract_inputs.fetch_input_file_data(INPUT_FILE)
    error_codes = extract_inputs.fetch_json_file_data(ERROR_CODE_FILE)
    standard_definition = extract_inputs.fetch_json_file_data(STANDARD_DEFINITION_FILE)

    error_code_dict = extract_inputs.convert_array_to_dict(error_codes, 'code', 'message_template')
    standard_definition_dict = extract_inputs.convert_array_to_dict(standard_definition, 'key', 'sub_sections')
    
    converted_report_list, summary_string = parse_input(input_data, error_code_dict, standard_definition_dict)
    
    write_results.write_report(REPORT_FILENAME, converted_report_list, CSV_REPORT_COLUMN_NAMES)
    write_results.write_summary(SUMMARY_FILENAME, summary_string)
    
     
if __name__ == '__main__':
    parse_bluenode_data()