# -*- coding: utf-8 -*-
# %%
import sys
import click

@click.command()
@click.option('--name', '-n', default='World')
def main(name):
    msg = 'Hello, {name}!'.format(name=name)
    click.echo(msg)