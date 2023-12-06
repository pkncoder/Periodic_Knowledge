import re
import csv

def findElement(userInput):

    if re.findall('[1-9]', userInput):
        with open('data.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                if row[0] == userInput:
                    return row
                
    elif len(userInput) <= 2:
        with open('data.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                if row[1].replace(' ', '').upper() == userInput.upper():
                    return row

    else:
        with open('data.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                if row[2].replace(' ', '').upper() == userInput.upper():
                    return row