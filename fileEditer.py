import csv

newfile = open('data.csv', 'w')

with open('dataold.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    total = 0
    for row in csv_reader:
        newfile.write(f'{row[0]}, {row[1]}, {row[2]}, {row[3]}, {row[7]}, {row[8]}, {row[9]}, {row[20]}, {row[21]}, {row[24]}, {row[10]}, {row[26]}, {row[27]}\n')

newfile.close()