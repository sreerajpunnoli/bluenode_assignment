# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 00:56:21 2021

@author: Sree
"""

#%%
from bluenode.load_settings import load_settings_obj
from bluenode.parse_data import parse_data_obj
from bluenode.write_results import write_results_obj

from extract_input_files import extract_input_files_obj

import logging
import os


REPORT_CSV_COLUMN_NAMES = 'Section,Sub-Section,Given DataType,Expected DataType,'\
                            'Given Length,Expected MaxLength,Error Code'.split(',')

# Initializing settings file location for modifying input file paths, output file paths, and input dictionary keys if required
SETTINGS_FILEPATH = os.path.join('config' ,'settings.yml')


def fetch_input_files(settings):
    ''' This method fetches the input_data, error_codes and standard_definition files '''
    logging.debug('Fetching input files')
    try:
        input_data = extract_input_files_obj.fetch_input_file_data(settings['input_file_path'])
        error_codes = extract_input_files_obj.fetch_json_file_data(settings['error_code_file_path'])
        standard_definition = extract_input_files_obj.fetch_json_file_data(settings['standard_definition_file_path'])
    except Exception as e:
        logging.error('Error while fetching input files', e)
        raise
    
    logging.debug('Fetched input files')
    return input_data, error_codes, standard_definition


def convert_lists_to_dicts(error_codes, standard_definition, settings):
    ''' This method converts error codes list and standard definition list to dictionaries '''
    
    logging.debug('Converting lists to dictionaries started')
    try:
        error_code_dict = extract_input_files_obj.convert_list_to_dict(error_codes, settings['error_code_key'], \
                                                                settings['error_code_value_key'])
        standard_definition_dict = extract_input_files_obj.convert_list_to_dict(standard_definition, settings['standard_definition_key'], \
                                                                settings['standard_definition_value_key'])
    except Exception as e:
        logging.error('Error while converting error codes and standard definition', e)
        raise
    
    logging.debug('Converted lists to dictionaries')
    return error_code_dict, standard_definition_dict


def write_parsed_results(converted_report_list, summary_string, settings):
    ''' Save parsed results '''
    
    logging.debug('Writing parsed results started')
    try:
        write_results_obj.write_report(settings['report_file_path'], converted_report_list, REPORT_CSV_COLUMN_NAMES)
        write_results_obj.write_summary(settings['summary_file_path'], summary_string)
    except Exception as e:
        logging.error('Error while writing the report and summary', e)
        raise
    logging.debug('Saved parsed results')


def parse_bluenode_data():
    logging.info('Bluenode data parsing started...')
    # Get file paths and dictionary keys
    settings = load_settings_obj.get_settings(SETTINGS_FILEPATH)
    
    # Fetch input files from the paths
    input_data, error_codes, standard_definition = fetch_input_files(settings)
    
    # Convert error_codes list and standard_definition list to dictionary
    error_code_dict, standard_definition_dict = convert_lists_to_dicts(error_codes, standard_definition, settings)
    
    # Parse input data
    converted_report_list, summary_string = parse_data_obj.parse_input(input_data, error_code_dict, standard_definition_dict)
    
    # Write parsed results
    write_parsed_results(converted_report_list, summary_string, settings)

    logging.info('Bluenode data parsing compled...')


if __name__ == '__main__':
    parse_bluenode_data()