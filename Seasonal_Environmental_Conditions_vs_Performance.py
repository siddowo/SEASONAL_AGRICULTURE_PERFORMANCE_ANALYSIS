import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('seasonal_agriculture_performance_dataset.csv')

# Scatter plot: Rainfall vs Yield colored by Season
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='Rainfall_mm', y='Yield_Tonnes_Ha', hue='Season', alpha=0.6, palette='bright')
plt.title('Impact of Environmental Rainfall on Yield by Season')
plt.xlabel('Rainfall (mm)')
plt.ylabel('Yield (Tonnes/Ha)')
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.savefig('q6_environmental_relationship.png')
plt.show()