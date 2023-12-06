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

def parseData(data):
    return (f'Name: {data[2]}\nSymbol: {data[1]}\nProtons: {data[0]}\nShells: {data[11]}\nValence Electrons: {data[12] if data[12] != " " else "No Known or Spesific Amount"}\nPeriod: {data[4]}\nGroup: {data[5] if data[5] != " " else "No Group"}\nBlock/Type: {data[13]}\nCommon State: {data[6]}\nAtomic Weight: {data[3]}\nRadioactive: {data[10] if data[10] != " " else "No"}\nMelting Point (Kelvin): {data[7]  if data[7] != " " else "No Known Melting Point"}\nBoiling Point (Kelvin): {data[8]  if data[7] != " " else "No Known Boiling Point"}\nYear Discovered: {data[9] if data[9] != " " else "Prehistoric"}')