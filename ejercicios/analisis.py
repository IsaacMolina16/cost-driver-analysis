import pandas as pd

# Crear datos de ejemplo (simulando una planta)
data = {
    'Machine': ['A', 'A', 'B', 'B', 'C', 'C'],
    'Shift': ['Dia', 'Noche', 'Dia', 'Noche', 'Dia', 'Noche'],
    'Production': [1000, 1100, 900, 950, 1200, 1150],
    'Scrap': [50, 80, 30, 60, 20, 25],
    
}


# 1️⃣ Crear DataFrame
df = pd.DataFrame(data)

# genera promedio de datos
df.groupby('Machine')['Scrap_Rate'].mean()

# 2️⃣ Eliminar duplicados
df = df.drop_duplicates()

# 3️⃣ Crear Scrap Rate
df['Scrap_Rate'] = df['Scrap'] / df['Production']

# Mostrar datos
print(df)