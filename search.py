# Import the liberaries needed
import re
import csv

# This function finds the user's element by matching their input
def findElement(userInput):

    # If there is a one to nine in their input, AND ALSO NO CHARACTERS then search with atomic number
    if userInput.isdigit():
        # Open the csv and use the csv reader so we can subscript
        with open('data.csv') as csv_file:

            # Store csv reader as the iterable object
            csv_reader = csv.reader(csv_file, delimiter=',')

            # Loop each row so we can iterate on each spot inside the row instead of just each row
            for row in csv_reader:
                
                # For every row, check the first slot
                # If it matches the user's input then return the whole row to get ready for parsing
                if row[0] == userInput:
                    return row
                
            # Now if it isn't any of these things, then somthing is wrong with the user's input
            # Direct them to do somthing else
            # Return the statement to be printed
            return 'There was either an error with running the code or your input, please try again and report an issue on github at https://github.com/pkncoder/Periodic_Knowledge.'
                
    # If the user's input is two or less, then it has to be a atomic symbol
    elif len(userInput) <= 2:
        # Open the csv and use the csv reader so we can subscript
        with open('data.csv') as csv_file:

            # Store csv reader as the iterable object            
            csv_reader = csv.reader(csv_file, delimiter=',')

            # Loop each row so we can iterate on each spot inside the row instead of just each row
            for row in csv_reader:

                # Check if the third spot in the row (atomic symbol) is equal to the user's input
                # Make everything uppercase so capitalization does not matter
                # Get rid of any spaces here incase there is any
                if row[2].replace(' ', '').upper() == userInput.upper():

                    # Return the whole row to get ready to parse through
                    return row

            # Now if it isn't any of these things, then somthing is wrong with the user's input
            # Direct them to do somthing else
            # Return the statement to be printed
            return 'There was either an error with running the code or your input, please try again and report an issue on github at https://github.com/pkncoder/Periodic_Knowledge.'

    # If it is not a number or a symbol, it has to be more than two
    # This is for name
    elif len(userInput) > 2:
        # Open the csv and use the csv reader so we can subscript
        with open('data.csv') as csv_file:

            # Store csv reader as the iterable object            
            csv_reader = csv.reader(csv_file, delimiter=',')

            # Loop each row so we can iterate on each spot inside the row instead of just each row
            for row in csv_reader:

                # Check if the second spot in the row (name) is equal to the user's input
                # Make everything uppercase so capitalization does not matter
                # Get rid of any spaces here incase there is any
                if row[1].replace(' ', '').upper() == userInput.upper():
                    # Return the whole row to get ready to parse through
                    return row
                
            # Now if it isn't any of these things, then somthing is wrong with the user's input
            # Direct them to do somthing else
            # Return the statement to be printed
            return 'There was either an error with running the code or your input, please try again and report an issue on github at https://github.com/pkncoder/Periodic_Knowledge.'

# Parse the data and return it as a dictionary
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