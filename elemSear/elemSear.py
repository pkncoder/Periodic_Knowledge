# Import get.py
import csv

# Import the click liberary
import click

# Make an overal group to hold everything
@click.group()
def cli():
    pass

# Make a find group to find things
@cli.group()
def find():
    pass

# Make a command with the find group to find elements with protons
@find.command()
@click.argument('protons')
def protons(protons):
    print(findWithProtons(protons))

# Make a command with the find group to find elements with symbol
@find.command()
@click.argument('symbol')
def symbol(symbol):
    print(findWithSymbol(symbol))

# Make a command with the find group to find elements with name
@find.command()
@click.argument('name')
def name(name):
    print(findWithName(name))


# Make a list group to list things
@cli.group(name='list')
def list_():
    pass

# When ran, run the cli group to make everything acessable
if __name__ == '__main__':
    cli()



# Make a function to find with protons
def findWithProtons(protons):
    # If the user inputs a didget, then let it through
    if protons.isdigit():
        # Open the csv and use the csv reader so we can subscript
        with open('data.csv') as csv_file:

            # Store csv reader as the iterable object
            csv_reader = csv.reader(csv_file, delimiter=',')

            # Loop each row so we can iterate on each spot inside the row instead of just each row
            for row in csv_reader:
                
                # For every row, check the first slot
                # If it matches the user's input then return the whole row to get ready for parsing
                if row[0] == protons:
                    return row
            
            # If no answer was found, return the error message
            return' There was either an error with running the code or your input, please try again and report an issue on github at https://github.com/pkncoder/Periodic_Knowledge.'
                
    # If it is not a didget, then return the error message
    else:
        return 'There was either an error with running the code or your input, please try again and report an issue on github at https://github.com/pkncoder/Periodic_Knowledge.'

# Make a function to find with symbol
def findWithSymbol(symbol):
    pass

# Make a function to find with name
def findWithName(name):
    pass