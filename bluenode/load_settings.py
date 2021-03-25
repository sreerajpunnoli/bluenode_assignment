# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 01:38:16 2021

@author: Sree
"""
import yaml
import os
import logging


class LoadSettings:
    
    def get_default_settings(self):
        ''' This method returns the default input file paths, output file paths, and input dictionary keys'''
        
        settings = {}
        # File paths
        settings['input_file_path'] = os.path.join('inputs', 'input_file.txt')    
        settings['error_code_file_path'] = os.path.join('inputs', 'error_codes.json')
        settings['standard_definition_file_path'] = os.path.join('inputs', 'standard_definition.json')
        settings['report_file_path'] = os.path.join('parsed', 'report.csv')
        settings['summary_file_path'] = os.path.join('parsed', 'summary.txt')
        
        # Dictionary keys
        settings['error_code_key'] = 'code'
        settings['error_code_value_key'] = 'message_template'
        settings['standard_definition_key'] = 'key'
        settings['standard_definition_value_key'] = 'sub_sections'
        
        return settings
        
    
    def get_settings(self, settings_file_path):
        ''' This method returns the input file paths, output file paths, and input dictionary keys as a dictionary '''
        try:
            settings = self.get_default_settings()
            if os.path.isfile(settings_file_path):
                with open(settings_file_path, 'r') as f:
                    settings_from_file = yaml.safe_load(f) or {}
                    settings.update(settings_from_file)
                    
                    logging.info('Setting extracted...')
        except:
            logging.warn("Could not parse the settings.yml file! Using the default settings")
            
        return settings
    
# Singleton object
load_settings_obj = LoadSettings()