from monthly_record import MonthlyRecord
from constants import MONTH_NAMES

class YearlyRecord:

    def __init__(self):
        self.months = dict()
        self.year = ''

    def highest_temperature_day(self):
        temp_and_day = [-1, -1, -1]             # 0 index max temp, 1 index day, 2 index month
        files_missing = 0

        # Looping to compare highest temperature days of each month
        for i in range(12):
            key = MONTH_NAMES[i]
            if not self.months[key]:
                files_missing += 1
                continue
            temp = self.months[key].max_temperature()
            if temp_and_day[0] < temp[0]:
                temp_and_day = temp
                temp_and_day.append(i)
        if files_missing == 12:
            return None
        return temp_and_day

    def lowest_temperature_day(self):
        temp_and_day = [9999, -1, -1]             # 0 index min temp, 1 index day, 2 index month
        files_missing = 0
        
        for i in range(12):
            key = MONTH_NAMES[i]
            if not self.months[key]:
                files_missing += 1
                continue
            temp = self.months[key].min_temperature()
            if temp_and_day[0] > temp[0]:
                temp_and_day = temp
                temp_and_day.append(i)
        if files_missing == 12:
            return None
        return temp_and_day

    def max_humidity_day(self):
        humidity_and_day = [-1, -1, -1]             # 0 index min temp, 1 index day, 2 index month
        files_missing = 0
        
        for i in range(12):
            key = MONTH_NAMES[i]
            if not self.months[key]:
                files_missing += 1
                continue
            temp = self.months[key].max_humidity()
            if humidity_and_day[0] < temp[0]:
                humidity_and_day = temp
                humidity_and_day.append(i)
        if files_missing == 12:
            return None
        return humidity_and_day