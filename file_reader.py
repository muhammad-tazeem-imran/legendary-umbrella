import csv
from monthly_record import MonthlyRecord
from yearly_record import YearlyRecord
from constants import MONTH_NAMES

class FileReader:

    def readMonthFile(self, file_path, month_no, year):
        month = MonthlyRecord()
        month.month_name = MONTH_NAMES[(int)(month_no)-1]
        file_path = file_path + 'Murree_weather_' + year + '_' + month.month_name[:3] + '.txt'
        try:
            with open(file_path, newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                count = 0
                for row in reader:
                    month.days.append(row)
                    count += 1
        except IOError:
            print("File not found:",file_path)
            return None
        return month

    def readYear(self, file_path, year):
        year_record = YearlyRecord()
        
        for i in range(12):
            key = MONTH_NAMES[i]
            year_record.months[key] = self.readMonthFile(file_path, i, year)

        return year_record