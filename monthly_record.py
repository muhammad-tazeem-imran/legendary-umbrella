class MonthlyRecord:

    def __init__(self):
        self.days=[]
        self.month_name = ''

    def max_temperature(self):
        max_temp = [0, 0]             # 0th element max temp, 1st element day
        count = 0

        # Each element in days is a dictionary representing a day's readings
        for i in self.days:
            if i["Max TemperatureC"] == '':
                continue
            temp_int = (int)(i["Max TemperatureC"])

            if temp_int > max_temp[0]:
                max_temp[0] = temp_int
                max_temp[1] = count
            count += 1
        return max_temp

    def min_temperature(self):
        min_temp = [9999, 0]
        count = 0

        # Each element in days is a dictionary representing a day's readings
        for i in self.days:
            if i["Min TemperatureC"] == '':
                continue
            temp_int = (int)(i["Min TemperatureC"])

            if temp_int < min_temp[0]:
                min_temp[0] = temp_int
                min_temp[1] = count
            count += 1
        return min_temp

    def max_humidity(self):
        max_humidity = [0, 0]             # 0th element max humidity, 1st element day
        count = 0

        # Each element in days is a dictionary representing a day's readings
        for i in self.days:
            if i["Max Humidity"] == '':
                continue
            humidity_int = (int)(i["Max Humidity"])
            if humidity_int > max_humidity[0]:
                max_humidity[0] = humidity_int
                max_humidity[1] = count
            count += 1
        return max_humidity

    def average_field_value(self,fieldName):
        sum_field = 0
        day_count = 0
        for i in self.days:
            if i[fieldName] != '':
                sum_field += (int)(i[fieldName])
                day_count += 1
        return sum_field/day_count
