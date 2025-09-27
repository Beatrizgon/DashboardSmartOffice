# resumo_smart_office.py
import pandas as pd

# Carregar CSV gerado pelo simulador
df = pd.read_csv("smart_office_data.csv")
df['timestamp'] = pd.to_datetime(df['timestamp'])

# Criar coluna com a data (sem hora)
df['date'] = df['timestamp'].dt.date

# Função para calcular resumo diário por sala e sensor
resumo_diario = []

for room in df['room'].unique():
    for date in df['date'].unique():
        df_day_room = df[(df['room'] == room) & (df['date'] == date)]
        
        # Temperatura média
        temp_mean = df_day_room[df_day_room['sensor_type']=='temperature']['value'].mean()
        
        # Luminosidade média
        lux_mean = df_day_room[df_day_room['sensor_type']=='luminosity']['value'].mean()
        
        # Pico de ocupação
        occupancy_max = df_day_room[df_day_room['sensor_type']=='occupancy']['value'].sum()
        
        resumo_diario.append({
            "date": date,
            "room": room,
            "avg_temperature": round(temp_mean,2),
            "avg_luminosity": round(lux_mean,2),
            "peak_occupancy": int(occupancy_max)
        })

# Criar DataFrame do resumo
df_resumo = pd.DataFrame(resumo_diario)

# Salvar CSV de resumo (opcional)
df_resumo.to_csv("smart_office_resumo.csv", index=False)

print("Resumo diário gerado: smart_office_resumo.csv")
print(df_resumo.head(10))  # mostrar as 10 primeiras linhas
