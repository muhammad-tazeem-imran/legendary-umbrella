import csv

with open('weatherfiles/Murree_weather_2004_Dec.txt',newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    count = 0
    for row in reader:
        print(row["PKT"],'\n')
        count += 1
    print("rows read : ",count)