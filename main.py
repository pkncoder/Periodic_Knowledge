from search import *
from sys import argv
from rich.console import Console
from rich.table import Table

data = parseData(findElement(argv[1]))

keys = list(data.keys())

table = Table(title=f"[bold]Values of {data['Name']}", show_lines=True)

table.add_column('[red]Key', style='red')
table.add_column('[cyan]Value', style='cyan') 

for i in range(len(data)):
    table.add_row(keys[i], data[keys[i]])

console = Console()
console.print(table)