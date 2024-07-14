import psutil
import click

def get_cpu_temperature():
    temps = psutil.sensors_temperatures()
    if not temps:
        return 'No temperature sensors found.'
    
    for name, entries in temps.items():
        for entry in entries:
            if entry.label == 'Package id 0' or not entry.label:
                temp = int(entry.current)
                
                return temperature_color(temp)

    return 'Unable to retrieve CPU temperature.'

def temperature_color(temperature):
    if temperature is not None:
        if temperature < 30:
            click.echo(click.style(f'CPU Temperature: {temperature}°C - Low', fg='blue'))
        elif temperature > 30 and temperature < 60:
            click.echo(click.style(f'CPU Temperature: {temperature}°C - Normal', fg='green'))
        elif temperature > 61 and temperature < 80:
            click.echo(click.style(f'CPU Temperature: {temperature}°C - High', fg='yellow'))
        elif temperature > 81:
            click.echo(click.style(f'CPU Temperature: {temperature}°C - Dangerous', fg='red'))
