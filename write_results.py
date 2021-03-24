# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 00:03:34 2021

@author: Sree
"""
import csv

#import csv
#with open(..., 'w', newline='') as myfile:
#     wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
#     wr.writerow(mylist)

def write_report(filename, report_list, csv_column_names):
    with open(filename, 'w') as f:
        write = csv.writer(f)
        
        write.writerow(csv_column_names)
        write.writerows(report_list)


def write_summary(filename, summary_string):
    with open(filename, 'w') as f:
        f.write(summary_string)
    
