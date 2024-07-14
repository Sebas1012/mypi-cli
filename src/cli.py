from src.temp import get_cpu_temperature
from src.net import get_network_info
import click

@click.group()
def cli():
    """
    Mypi-cli: Is a CLI that allows you to abstract some tedious tasks in OrangePi into simple commands.
    """
    pass

@cli.command()
def temp():
   """ View current CPU temperature. """
   get_cpu_temperature()
    
@cli.command()
def net():
    """ Allows you to view current network information. """
    get_network_info()