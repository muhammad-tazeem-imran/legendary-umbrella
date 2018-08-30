#!./fTask/bin/python

import re
import sys
from constants import ERROR_MSG, ERROR_MSG_2

from report import Report


if (len(sys.argv)%2 != 0) or len(sys.argv)<4:
    print(ERROR_MSG)
    exit()
files_directory = sys.argv[1]
if files_directory[-1] != '/':
    files_directory = files_directory + '/'

report_type = []
report_specs = []
monthly_report = False
yearly_report = False



i = 2                   # 0 and 1 locations contain name and file directory
while i < len(sys.argv):
    if re.match(r'-[ac]$',sys.argv[i]):         # Check for monthly report
        report_type.append(sys.argv[i])
        i += 1

        # Matching pattern xxxx/xx
        if (re.match(r'\d{4}/(0?[1-9]$|1[0-2]$)',sys.argv[i])):
            report_specs.append(sys.argv[i])
            i += 1
        else:
            print(ERROR_MSG_2)
            report_type.pop()
            i += 1
    elif re.match(r'-e$',sys.argv[i]):          # Check for yearly report
        report_type.append(sys.argv[i])
        i += 1

        # Matching pattern xxxx
        if (re.match(r'\d{4}$',sys.argv[i])):
            report_specs.append(sys.argv[i])
            i += 1
        else:
            print(ERROR_MSG_2)
            report_type.pop()
            i += 1
    else:
        print(ERROR_MSG_2)
        i += 2

report = Report(files_directory)
report.create_reports(report_type, report_specs)