# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 00:03:34 2021

@author: Sree
"""
import csv

class WriteResults:
    
    def write_report(self, filename, report_list, csv_column_names):
        with open(filename, 'w', newline='') as f:
            write = csv.writer(f)
            write.writerow([])
            write.writerow(csv_column_names)
            write.writerows(report_list)
    
    
    def write_summary(self, filename, summary_string):
        with open(filename, 'w') as f:
            f.write(summary_string)

# Singleton object
write_results_obj = WriteResults()
