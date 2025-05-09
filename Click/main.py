import click
from datetime import datetime

@click.group()
def cli():
    pass

@cli.command()
@click.option("--count", default=1, help="Number of greetings.")
@click.option("--name", prompt="Your name", help="The person to greet.")
def hello(count, name):
    """Simple program that greets NAME for a total of COUNT times."""
    for _ in range(count):
        print(f"Hello, {name}!")
@cli.command()
def time():
    now = datetime.now()
    print("Current time:", now.strftime("%H:%M:%S"))

@cli.command()
def triste():
    print(":(")

@cli.command()
def feliz():
    print(":)")



if __name__ == '__main__':
    cli()