#%%
import os
import csv
import unittest
import sys

path_list = os.getcwd().split(os.sep)[:-1]
parent_path = os.sep.join(path_list)
if parent_path not in sys.path:
    sys.path.append(parent_path)

import parse_bluenode_data

settings = {}
converted_report_list = []
summary_string = ''


def get_test_settings():
    settings = {}
    # File paths
    settings['input_file_path'] = os.path.join('tests', 'sample', 'input', 'input_file.txt')    
    settings['error_code_file_path'] = os.path.join('inputs', 'error_codes.json')
    settings['standard_definition_file_path'] = os.path.join('inputs', 'standard_definition.json')
    settings['report_file_path'] = os.path.join('tests', 'sample', 'parsed', 'report.csv')
    settings['summary_file_path'] = os.path.join('tests', 'sample', 'parsed', 'summary.txt')
    
    # Dictionary keys
    settings['error_code_key'] = 'code'
    settings['error_code_value_key'] = 'message_template'
    settings['standard_definition_key'] = 'key'
    settings['standard_definition_value_key'] = 'sub_sections'
    
    return settings


def get_parsed_data(settings):
    input_data, error_codes, standard_definition = parse_bluenode_data.fetch_input_files(settings)
    error_code_dict, standard_definition_dict = parse_bluenode_data.convert_lists_to_dicts(error_codes, standard_definition, settings)
    converted_report_list, summary_string = parse_bluenode_data.parse_data_obj.parse_input(input_data, error_code_dict, standard_definition_dict)
    
    return converted_report_list, summary_string


def get_stored_report(settings):
    converted_stored_report = []
    with open(settings['report_file_path'], newline='') as f:
        reader = csv.reader(f)
        stored_report = list(reader)
        for row in stored_report[2:]:
            row[-2] = int(row[-2]) if row[-2] else ''
            row[-3] = int(row[-3]) if row[-3] else ''
            converted_stored_report.append(row)
    return converted_stored_report


def get_stored_summary(settings):
    with open(settings['summary_file_path'], 'r') as f:
        stored_summary = f.read()
    return stored_summary


class ParseTest(unittest.TestCase):
        
    def test_report(self):        
        stored_report = get_stored_report(settings)
        self.assertEqual(stored_report, converted_report_list, "Report not parsed properly!")
        

    def test_summary(self):
        stored_summary = get_stored_summary(settings)
        self.assertEqual(stored_summary, summary_string, "Summary not parsed properly!")
        
if __name__ == '__main__':
    global settings, converted_report_list, summary_string
    
    settings = get_test_settings()
    converted_report_list, summary_string = get_parsed_data(settings)
    
    unittest.main()