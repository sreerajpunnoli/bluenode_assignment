#%%
import os
import csv
import unittest
#import sys
#path_list = os.getcwd().split(os.sep)[:-1]
#parent_path = os.sep.join(path_list)
#if parent_path not in sys.path:
#    sys.path.append(parent_path)
import parse_bluenode_data

def get_test_settings():
    settings = {}
    # File paths
    settings['input_file_path'] = os.path.join('tests', 'sample', 'inputs', 'input_file.txt')    
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
    with open(settings['report_file_path'], newline='') as f:
        reader = csv.reader(f)
        stored_report = list(reader)
    return stored_report[2:]


def get_stored_summary(settings):
    with open(settings['summary_file_path'], 'r') as f:
        stored_summary = f.read()
    return stored_summary


class ParseTest(unittest.TestCase):

    def test_report(self, settings, report):
        stored_report = get_stored_report(settings)
        self.assertEqual(stored_report, report, "Report not parsed properly!")

    def test_summary(self, settings, summary):
        stored_summary = get_stored_summary(settings)
        self.assertEqual(stored_summary, summary, "Summary not parsed properly!")
        
    def get_inputs(self):
        settings = get_test_settings()
        converted_report_list, summary_string = get_parsed_data(settings)
        self.test_report(settings, converted_report_list)
        self.test_summary(settings, summary_string)


if __name__ == '__main__':
    unittest.main()