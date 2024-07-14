import psutil

def get_cpu_temperature():
    temps = psutil.sensors_temperatures()
    if not temps:
        return "No se encontraron sensores de temperatura."
    
    for name, entries in temps.items():
        for entry in entries:
            if entry.label == 'Package id 0' or not entry.label:
                return f"Temperatura de la CPU: {entry.current} °C"
    return "No se encontró la temperatura de la CPU."
