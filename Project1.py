import pandas as pd
import matplotlib.pyplot as plt
import os

# Show files in directory (debugging)
print("Files in directory:", os.listdir())

# =========================
# Load Data
# =========================
df = pd.read_excel('clean_data.xlsx')

# =========================
# SORT FOR PARETO
# =========================
df = df.sort_values(by='Cost', ascending=False)

# Calculate cumulative percentage
df['Cumulative_Percentage'] = df['Cost'].cumsum() / df['Cost'].sum() * 100

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

plt.savefig("pareto_chart.png")
plt.show()

# =========================
# SCATTER PLOT (QUADRANT ANALYSIS)
# =========================
plt.figure()

plt.scatter(df['Failed'], df['Cost'])

mean_failed = df['Failed'].mean()
mean_cost = df['Cost'].mean()

plt.axvline(mean_failed, linestyle='--')
plt.axhline(mean_cost, linestyle='--')

# Annotate each point with component name
for i, component in enumerate(df['Component']):
    plt.annotate(component, (df['Failed'].iloc[i], df['Cost'].iloc[i]))

plt.xlabel("Number of Failures")
plt.ylabel("Cost (USD)")
plt.title("Failure Frequency vs Cost Impact")

plt.tight_layout()
plt.savefig("scatter_plot.png")
plt.show()

# =========================
# ROI ANALYSIS
# =========================
df['ROI'] = df['Avoided'] / df['Cost']

roi_sorted = df[['Component', 'ROI']].sort_values(by='ROI', ascending=False)

print("\nTop ROI Components:\n")
print(roi_sorted)