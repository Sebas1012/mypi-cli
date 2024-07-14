import subprocess
import time
import click

def get_cpu_temperature():
    result = subprocess.run(['sensors'], capture_output=True)
    output = result.stdout.decode('utf-8')
    temperature = output.splitlines()[2].split()[1].strip('°C')
    return temperature

while True:
    cpu_temperature = get_cpu_temperature()
    click.echo(f"CPU Temperature: {cpu_temperature} °C")
    time.sleep(5)