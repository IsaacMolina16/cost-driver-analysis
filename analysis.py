import pandas as pd
import matplotlib.pyplot as plt
import os

# =========================
# CONFIG
# =========================
DATA_PATH = 'clean_data.xlsx'
OUTPUT_PATH = 'outputs'

os.makedirs(OUTPUT_PATH, exist_ok=True)

# =========================
# LOAD DATA
# =========================
df = pd.read_excel(DATA_PATH)

# Sort for Pareto
df = df.sort_values(by='Cost', ascending=False).reset_index(drop=True)

# =========================
# FEATURE ENGINEERING
# =========================
df['Cumulative_Percentage'] = df['Cost'].cumsum() / df['Cost'].sum() * 100
df['ROI'] = df['Avoided'] / df['Cost']

# =========================
# PARETO CHART
# =========================
fig, ax1 = plt.subplots()

ax1.bar(df['Component'], df['Cost'])
ax1.set_xlabel("Component")
ax1.set_ylabel("Cost (USD)")
plt.xticks(rotation=90)

ax2 = ax1.twinx()
ax2.plot(df['Component'], df['Cumulative_Percentage'], marker='o')
ax2.set_ylabel("Cumulative %")

plt.title("Pareto Analysis - Repair Cost Drivers")
plt.tight_layout()
plt.savefig(f"{OUTPUT_PATH}/pareto_chart.png")
plt.close()

# =========================
# SCATTER PLOT
# =========================
plt.figure()

plt.scatter(df['Failed'], df['Cost'])

mean_failed = df['Failed'].mean()
mean_cost = df['Cost'].mean()

plt.axvline(mean_failed, linestyle='--')
plt.axhline(mean_cost, linestyle='--')

# Annotate top 10 only
for i, component in enumerate(df['Component']):
    if i < 10:
        plt.annotate(component, (df['Failed'].iloc[i], df['Cost'].iloc[i]))

plt.xlabel("Number of Failures")
plt.ylabel("Cost (USD)")
plt.title("Failure Frequency vs Cost Impact")

plt.tight_layout()
plt.savefig(f"{OUTPUT_PATH}/scatter_plot.png")
plt.close()

# =========================
# INSIGHTS OUTPUT
# =========================
top_cost = df.head(3)
top_roi = df.sort_values(by='ROI', ascending=False).head(3)

print("\n=== TOP COST DRIVERS ===")
print(top_cost[['Component', 'Cost']])

print("\n=== TOP ROI COMPONENTS ===")
print(top_roi[['Component', 'ROI']])

print("\n=== SUMMARY ===")
print(f"Total Cost: ${df['Cost'].sum():,.2f}")
print(f"Average Cost: ${df['Cost'].mean():,.2f}")
