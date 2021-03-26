#%%
import os
import csv
import unittest
import parse_bluenode_data


settings = {}
calculated_report_list = []
calculated_summary_string = ''


def get_test_settings():
    ''' Get unit test settings '''
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
    ''' Read sample input files and defnitions and calculate the results using the bluenode module '''
    input_data, error_codes, standard_definition = parse_bluenode_data.fetch_input_files(settings)
    error_code_dict, standard_definition_dict = parse_bluenode_data.convert_lists_to_dicts(error_codes, standard_definition, settings)
    converted_report_list, summary_string = parse_bluenode_data.parse_data_obj.parse_input(input_data, error_code_dict, standard_definition_dict)
    
    return converted_report_list, summary_string


def get_stored_report(settings):
    ''' Get the stored report csv content as list '''
    stored_report = []
    with open(settings['report_file_path'], newline='') as f:
        reader = csv.reader(f)
        report = list(reader)
        # Avoid the header
        for row in report[2:]:
            # Convert the length columns to integers
            row[-2] = int(row[-2]) if row[-2] else ''
            row[-3] = int(row[-3]) if row[-3] else ''
            stored_report.append(row)
    return stored_report


def get_stored_summary(settings):
    ''' Get the storeed summary content as string '''
    with open(settings['summary_file_path'], 'r') as f:
        stored_summary = f.read()
    return stored_summary


class ParseTest(unittest.TestCase):
        
    def test_report(self):        
        stored_report = get_stored_report(settings)
        self.assertEqual(stored_report, calculated_report_list, "Report not parsed properly!")

    def test_summary(self):
        stored_summary = get_stored_summary(settings)
        self.assertEqual(stored_summary, calculated_summary_string, "Summary not parsed properly!")


if __name__ == '__main__':   
    settings = get_test_settings()
    # Calculate the reports and summary to compare it with already stored report and summary
    calculated_report_list, calculated_summary_string = get_parsed_data(settings)
    
    unittest.main()