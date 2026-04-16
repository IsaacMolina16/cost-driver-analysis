import pandas as pd

df = pd.read_excel('datos_limpios.xlsx')

print(df.head())

print(df['Cost'])

print(df[df['Cost'] > 100000])