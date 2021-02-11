#!/usr/bin/env python
import click
from hello import with_input

@click.command()
@click.option('--color', help="This is your fav color")
def callcolor(color):
    result = with_input(color)
    statement = f"""
    My favorite is: {result["old"]}.
    I also like result: {result["new"]}
    """
    click.echo(click.style(statement,bg='red', fg="blue"))

if __name__ == '__main__':
    #pylint: disable=no-value-for-parameter
    callcolor()
