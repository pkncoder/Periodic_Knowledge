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
                if row[2].replace(' ', '').upper() == userInput.upper():
                    return row

    elif len(userInput) > 2:
        with open('data.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                if row[1].replace(' ', '').upper() == userInput.upper():
                    return row

def parseData(data):
    return \
    {
        'Name': data[1],
        'Symbol': data[2],
        'Protons': ' ' + data[0],
        'Shells': data[11],
        'Valence Electrons': data[12] if data[12] != " " else " No Known or Spesific Amount",
        'Period': data[4],
        'Group': data[5] if data[5] != " " else " No Group",
        'Block/Type': data[13].title() if data[13] != " " else " Not Classified or Unkown",
        'Common State': data[6].title(),
        'Atomic Weight': data[3],
        'Radioactive': data[10].title() if data[10] != " " else " No",
        'Melting Point (Kelvin)': data[7]  if data[7] != " " else " No Known Melting Point",
        'Boiling Point (Kelvin)': data[8]  if data[8] != " " else " No Known Boiling Point",
        'Year Discovered': data[9] if data[9] != " " else " Prehistoric",
    }