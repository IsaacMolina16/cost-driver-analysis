import pandas as pd
import matplotlib.pyplot as plt
import os
print(os.listdir())

print("Archivos en carpeta:", os.listdir())

# =========================
# Cargar datos
# =========================
df = pd.read_excel('datos_limpios.xlsx')

# =========================
# ORDENAR PARA PARETO
# =========================
df = df.sort_values(by='Cost', ascending=False)

# Calcular porcentaje acumulado
df['Cum_Percentage'] = df['Cost'].cumsum() / df['Cost'].sum() * 100

# =========================
# PARETO
# =========================
fig, ax1 = plt.subplots()

ax1.bar(df['Component'], df['Cost'])
ax1.set_xlabel("Component")
ax1.set_ylabel("Cost (USD)")
plt.xticks(rotation=90)

ax2 = ax1.twinx()
ax2.plot(df['Component'], df['Cum_Percentage'], marker='o')
ax2.set_ylabel("Cumulative %")

plt.title("Pareto Analysis - Repair Cost Drivers")
plt.tight_layout()

plt.savefig("pareto_chart.png")  # 🔥 CLAVE
plt.show()

# =========================
# CUADRANTES (SCATTER)
# =========================
plt.figure()

plt.scatter(df['Failed'], df['Cost'])

mean_failed = df['Failed'].mean()
mean_cost = df['Cost'].mean()

plt.axvline(mean_failed, linestyle='--')
plt.axhline(mean_cost, linestyle='--')

for i, txt in enumerate(df['Component']):
    plt.annotate(txt, (df['Failed'].iloc[i], df['Cost'].iloc[i]))

plt.xlabel("Failures")
plt.ylabel("Cost (USD)")
plt.title("Failure vs Cost Matrix")

plt.tight_layout()
plt.savefig("scatter_plot.png")  # 🔥 CLAVE
plt.show()

# =========================
# ROI
# =========================
df['ROI'] = df['Avoided'] / df['Cost']

roi_sorted = df[['Component', 'ROI']].sort_values(by='ROI', ascending=False)

print("\nTop ROI Components:\n")
print(roi_sorted)