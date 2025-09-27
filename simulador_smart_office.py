# simulador_smart_office_v2.py
# Gera dados simulados para sensores de temperatura, luminosidade e ocupação
# para 4 salas, em intervalos de 15 minutos por 7 dias.
# Resultado: smart_office_data.csv

import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Configurações
start_date = datetime(2025, 9, 15, 0, 0)
period_days = 7
freq_minutes = 15
rooms = ["Sala_Reuniao", "Escritorio_A", "Escritorio_B", "Copa"]
sensor_types = ["temperature", "luminosity", "occupancy"]

# Função de temperatura lógica
def generate_temperature(ts, room):
    base_room = {"Sala_Reuniao": 22, "Escritorio_A": 22.5, "Escritorio_B": 22, "Copa": 21.5}[room]
    hour = ts.hour + ts.minute / 60.0
    diurnal = 2.5 * np.sin((hour - 4)/24 * 2*np.pi)  # mínima de madrugada, máxima à tarde
    noise = np.random.normal(0, 0.3)
    temp = base_room + diurnal + noise
    return round(max(18, min(temp, 27)), 2)  # limites 18-27°C

# Função de luminosidade lógica
def generate_lux(ts, room):
    hour = ts.hour + ts.minute / 60.0
    if 6 <= hour < 18:  # dia
        daylight = 200 + 800 * np.sin((hour - 6)/12 * np.pi)
        lights = np.random.uniform(50, 200)
        return int(max(0, daylight + lights + np.random.normal(0,20)))
    else:  # noite
        return int(max(0, np.random.normal(0,5)))

# Função de ocupação lógica
def generate_occupancy(ts, room):
    weekday = ts.weekday() < 5  # segunda=0 ... sexta=4
    hour = ts.hour + ts.minute/60.0
    base = {"Sala_Reuniao": 0.05, "Escritorio_A": 0.2, "Escritorio_B": 0.2, "Copa": 0.02}[room]

    if weekday and 8 <= hour < 18:  # horário comercial
        if room == "Sala_Reuniao":
            p = 0.15
        elif "Escritorio" in room:
            p = 0.6
        else:
            p = 0.25
    else:  # noite ou fim de semana
        p = base * (0.2 if not weekday else 0.4)
    return 1 if np.random.rand() < p else 0

# Construção de timestamps
n_records = int((period_days * 24 * 60) / freq_minutes)
timestamps = [start_date + timedelta(minutes=freq_minutes * i) for i in range(n_records)]

# Geração de dados
rows = []
sensor_id_counter = 0
for room in rooms:
    for sensor in sensor_types:
        sensor_id_counter += 1
        sid = f"{sensor[:3].upper()}_{room[:3].upper()}_{sensor_id_counter:02d}"
        for ts in timestamps:
            if sensor == "temperature":
                value = generate_temperature(ts, room)
            elif sensor == "luminosity":
                value = generate_lux(ts, room)
            elif sensor == "occupancy":
                value = generate_occupancy(ts, room)
            rows.append({
                "timestamp": ts,
                "sensor_id": sid,
                "sensor_type": sensor,
                "room": room,
                "value": value
            })

# Criação do DataFrame e exportação CSV
df = pd.DataFrame(rows)
df.to_csv("smart_office_data.csv", index=False)

print("Arquivo gerado: smart_office_data.csv")
