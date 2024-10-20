import csv
import numpy
with open("csv.csv", "r") as file:
    reader = csv.reader(csvfile=file, dialect="csv")
for row in reader():
    csv.proccess()