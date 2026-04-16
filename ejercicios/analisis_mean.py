import pandas as pd

data = {
    'Machine': ['A', 'A', 'B', 'B', 'C', 'C'],
    'Shift': ['Dia', 'Noche', 'Dia', 'Noche', 'Dia', 'Noche'],
    'Production': [1000, 1100, 900, 950, 1200, 1150],
    'Scrap': [50, 80, 30, 60, 20, 25]
}

# 1️⃣ Crear DataFrame
df = pd.DataFrame(data)

# 2️⃣ Crear Scrap Rate (ESTO VA PRIMERO)
df['Scrap_Rate'] = df['Scrap'] / df['Production']

#3️⃣ Agrupar por Machine + Shift
result = df.groupby(['Machine', 'Shift'])['Scrap_Rate'].mean()

#3.1 Ordena Resultados
#df.groupby(['Machine','Shift'])['Scrap_Rate'].mean().sort_values(ascending=False)

# 4️⃣ Imprimir
print(result)