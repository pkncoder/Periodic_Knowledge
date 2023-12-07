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
    print(protons)

# Make a command with the find group to find elements with symbol
@find.command()
@click.argument('symbol')
def symbol(symbol):
    print(symbol)

# Make a command with the find group to find elements with name
@find.command()
@click.argument('name')
def name(name):
    print(name)


# Make a list group to list things
@cli.group(name='list')
def list_():
    pass

# When ran, run the cli group to make everything acessable
if __name__ == '__main__':
    cli()