# Import our functions from search.py
from search import findElement, parseData

# Import needed liberaries
from sys import argv
from rich.console import Console
from rich.table import Table

# Get our data by running find element on the user's given argument in the terminal with argv
# Parse the data and get our dictionary
data = parseData(findElement(argv[1]))

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

# Make the console object and print the table with console.print()
console = Console()
console.print(table)