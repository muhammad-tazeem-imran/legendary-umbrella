from yearly_record import YearlyRecord
from file_reader import FileReader
from monthly_record import MonthlyRecord

from constants import MONTH_NAMES, COLOR_BLUE, COLOR_NORM, COLOR_RED

class Report:
    
    def __init__(self, files_path):
        self.files_directory = files_path

    def create_reports(self, report_type, report_specs):
        for i in range(len(report_specs)):
            if report_type[i] == '-e':                       # Creating yearly Report
                self.yearly_report(report_specs[i])
            elif report_type[i] == '-a':                     # Creating monthly report
                self.monthly_report(report_specs[i])
            elif report_type[i] == '-c':                     # Creating monthly graph
                self.monthly_graph(report_specs[i])
            print('\n----------------------------------\n')

    def monthly_report(self,report_specs):
        year = report_specs[0:4]
        month_no = report_specs[5:]
        month = MONTH_NAMES[(int)(month_no)-1]
        print(month,", ",year, sep = '')
        f = FileReader()
        read_month = f.readMonthFile(self.files_directory, month_no, year)
        if read_month:
            print('Highest Average: ', 
                round(read_month.average_field_value('Max TemperatureC'), 2),
                'C', sep = '')
            print('Lowest Average: ',
                round(read_month.average_field_value('Min TemperatureC'), 2),
                'C', sep = '')
            print('Average Mean Humidity: ', 
                round(read_month.average_field_value(' Mean Humidity'), 2),
                '%', sep = '')
        
    def monthly_graph(self, report_specs):
        year = report_specs[0:4]
        month_no = report_specs[5:]
        month = MONTH_NAMES[(int)(month_no)-1]
        print(month,", ",year, sep = '')
        f = FileReader()
        read_month = f.readMonthFile(self.files_directory, month_no, year)
        num = 1
        for i in read_month.days:
            output = str(num).rjust(2, '0')
            print(output + " ", end = '')
            if i["Max TemperatureC"] != '':
                max_temp = (int)(i["Max TemperatureC"])
            else:
                max_temp = 0
            if i["Min TemperatureC"] != '':
                min_temp = (int)(i["Min TemperatureC"])
            else:
                min_temp = 0
            output = '+' * min_temp
            print(COLOR_BLUE + output + COLOR_NORM, sep = '', end = '')
            
            output = '+' * max_temp 
            print(COLOR_RED + output + COLOR_NORM, sep = '', end = '')
            print(" ", min_temp, 'C -', max_temp, 'C', sep='')
            num += 1

    def yearly_report(self, report_specs):
        year = report_specs[0:4]
        f = FileReader()
        read_year = f.readYear(self.files_directory, year)
        max_temperature = read_year.highest_temperature_day()
        print('Year ', year, sep = '')
        if max_temperature:
            highest_temp = max_temperature[0]
            highest_day = max_temperature[1]
            highest_month = max_temperature[2]
            print("Highest: ",highest_temp,"C on ", 
                MONTH_NAMES[highest_month-1], " ", highest_day + 1, sep = '')

        min_temperature = read_year.lowest_temperature_day()
        if min_temperature:
            lowest_temp = min_temperature[0]
            lowest_day = min_temperature[1]
            lowest_month = min_temperature[2]
            print("Lowest: ",lowest_temp,"C on ", 
                MONTH_NAMES[lowest_month-1], " ", lowest_day + 1, sep = '')

        max_humidity = read_year.max_humidity_day()
        if max_humidity:
            highest_humidity = max_humidity[0]
            highest_day = max_humidity[1]
            highest_month = max_humidity[2]
            print("Humidity: ",highest_humidity,"% on ", 
                MONTH_NAMES[highest_month-1], " ", highest_day + 1, sep = '')
        