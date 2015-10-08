import csv

data = csv.reader(open("weather.csv", "rU"), dialect=csv.excel)

data.next()

for row in data:
    if row[2] < 30:
        temp = "It's cold"
    elif row[2] >=30 and row[2] <= 80:
        temp = "It's alright."
    else:
        temp = "It's hot."  
    print temp