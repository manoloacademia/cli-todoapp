""" This file builds a CLI To-Do App in python. """

# Import all libraries
from email.policy import default
import click

# Define the available priorities to the items
PRIORITIES = {
    "o": "Optional",
    "l": "Low",
    "m": "Medium",
    "h": "High",
    "c": "Crucial"
} 

# Define the group of commands
@click.group()
def mycommands():
    pass

# Define the command functions

@click.command()
@click.argument("priority", type=click.Choice(PRIORITIES.keys()), default="m")
@click.argument("todofile", type=click.Path(exists=False), required=0)
@click.option("-n", "--name", prompt="Write the name of the item", help="This is the name of the item")
@click.option("-d", "--description", prompt="Describe the item purpose", help="This is the description of the item")
def add_item(name, description, priority, todofile):
    filename = todofile if todofile is not None else "mytodos.txt"
    with open(filename, "a+") as f:
        f.write(f"{name}: {description} [Priority: {PRIORITIES[priority]}]\n")

@click.command()
@click.argument("idx", type=int, required=1)
def delete_item(idx):
    with open("mytodos.txt", "r") as f:
        items_list = f.read().splitlines()
        items_list.pop(idx)
    with open("mytodos.txt", "w") as f:
        f.write("\n".join(items_list))
        f.write("\n")

@click.command()
@click.argument("todofile", type=click.Path(exists=True), required=0)
@click.option("-p", "--priority", type=click.Choice(PRIORITIES.keys()))
def items_list(priority, todofile):
    filename = todofile if todofile is not None else "mytodos.txt"
    with open(filename, "r") as f:
        items = f.read().splitlines()
    if priority is None:    
        for idx, item in enumerate(items):
            print(f"{idx} - {item}")
    else:
        for idx, item in enumerate(items):
            if f"[Priority: {PRIORITIES[priority]}]" in item:
                print(f"{idx} - {item}")


# Add all commands to the group
mycommands.add_command(add_item)
mycommands.add_command(delete_item)
mycommands.add_command(items_list)

# At running the program
if __name__ == '__main__':
    mycommands()


