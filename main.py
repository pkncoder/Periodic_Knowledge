from Table import *
from sys import argv
import csv
#print(findElement(argv[1]))

with open('data.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        print(f'{row[0]}')
        print(f'{row[1]}')