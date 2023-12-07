# Import our functions from search.py
from search import findElement, parseData

# Import needed liberaries
from sys import argv
from rich.console import Console
from rich.table import Table

# Get our data by running find element on the user's given argument in the terminal with argv
possible_pre_parse_element_data = findElement(argv[1])

# Make the console object so the scope is bigger
console = Console()

# Check to make sure that possible pre parse element data isn't an error message by checking to see if it's a list
if type(possible_pre_parse_element_data) == list:

    # Parse the data after we made sure it isn't an error message
    data = parseData(possible_pre_parse_element_data)

    # Get the keys from the dictionary
    keys = list(data.keys())

    # Initialize our table with lines included
    table = Table(title=f"[bold]Values of {data['Name']}", show_lines=True)

    # Add the key and value columns
    table.add_column('[red]Key', style='red')
    table.add_column('[cyan]Value', style='cyan') 

    # Loop the entire length of the dictionary
    for i in range(len(data)):

        # For each key value pair add a row in the table of the current key, and the value of that current key
        table.add_row(keys[i], data[keys[i]])

    # Print the table with console.print
    console.print(table)

# If it is anything else, just print the error message
else:

    # Set the [insert large var name] as error message for readabilty
    # Don't have to do this but my code my choice
    error_message = possible_pre_parse_element_data
    
    # Print the error message, stylized
    console.print(f'[bold]{error_message}', style='red')