# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 01:48:18 2021

@author: Sree
"""
from bluenode.extract_fields import extact_fields_obj


class ParseData:
    
    def get_other_fields(self, row_array, index, expected_data_type, expected_max_length):
        ''' Returns given data type, length, and error code '''
        if index >= len(row_array):
            # If sub section data is missing, get missing default fileds
            given_data_type, given_length, error_code = extact_fields_obj.get_missing_default_fields()
        elif row_array[index] == '':
            # If sub section is empty, get empty default fileds
            given_data_type, given_length, error_code = extact_fields_obj.get_empty_default_fields()
        else:
            # Extract fields from row
            given_data_type = extact_fields_obj.get_data_type(row_array, index)
            given_length = extact_fields_obj.get_given_lenth(row_array, index)
            error_code = extact_fields_obj.get_error_code(expected_data_type, given_data_type, expected_max_length, given_length)
        
        return given_data_type, given_length, error_code
    
    def parse_input(self, input_data, error_code_dict, standard_definition_dict):
        ''' This method parse the input data using error code dict and standard definition dict
                and returns report list and summary string '''
        converted_report_list = []
        summary = ''
        
        for row in input_data:
            try:
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
                    
                    given_data_type, given_length, error_code = self.get_other_fields(row_array, index, \
                                                                        expected_data_type, expected_max_length)
                    
                    # Report row creation
                    row = [section, sub_section, given_data_type, expected_data_type, \
                                       given_length, expected_max_length, error_code]
                    converted_report_list.append(row)
                    
                    # Summary row creation
                    row_summary = error_code_dict[error_code].replace('LXY', sub_section) \
                                    .replace('LX', section).replace('{data_type}', expected_data_type) \
                                    .replace('{max_length}', str(expected_max_length))
                    # add new line charactor after each subsection
                    summary += row_summary + '\n'
                
                # add new line charactor after each section
                summary += '\n'
            except:
                pass
        # Remove two unwanted new line charactor from the end
        summary = summary[:-2]

        return converted_report_list, summary


# Singleton Object
parse_data_obj = ParseData()