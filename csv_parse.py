import csv
with open('input.csv', newline='') as csvfile:
    inputreader = csv.reader(csvfile, delimiter=';')
    for row in inputreader:
        print(', '.join(row))
