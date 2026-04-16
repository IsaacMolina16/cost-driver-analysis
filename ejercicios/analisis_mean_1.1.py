import pandas as pd

data = {
    'Machine': ['A', 'A', 'B', 'B', 'C', 'C'],
    'Shift': ['Dia', 'Noche', 'Dia', 'Noche', 'Dia', 'Noche'],
    'Production': [1000, 1100, 900, 950, 1200, 1150],
    'Scrap': [50, 80, 30, 60, 20, 25]
}

# 1️⃣ Crear DataFrame
df = pd.DataFrame(data)

# 2️⃣ Crear Scrap Rate
df['Scrap_Rate'] = df['Scrap'] / df['Production']

# 3️⃣ Crear Loss (💰)
df['Loss'] = df['Scrap'] * 10

# 4️⃣ Agrupar por Machine + Shift (LO NUEVO)
result = df.groupby(['Machine','Shift'])['Loss'].sum().sort_values(ascending=False)

# 5️⃣ Imprimir resultado
print(result)