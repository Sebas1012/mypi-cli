from colorama import init, Fore
from .temp import get_cpu_temperature
import click
import os

init(autoreset=True)

@click.group()
def cli():
    pass

@cli.command()
def temp():
    get_cpu_temperature()
    