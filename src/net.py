import psutil
import click

def get_network_info():
    interfaces = psutil.net_if_addrs()
    for interface_name, addresses in interfaces.items():
        for address in addresses:
            if address.family == 2:
                click.echo(f"Interface: {interface_name}\nAddress: {address.address}\nNetmask: {address.netmask}\nGateway: {address.broadcast}\n")