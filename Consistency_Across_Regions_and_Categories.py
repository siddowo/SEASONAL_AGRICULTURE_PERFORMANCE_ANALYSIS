import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('seasonal_agriculture_performance_dataset.csv')

# Pivot table: Yield across State and Season
state_season = df.groupby(['State', 'Season'])['Yield_Tonnes_Ha'].mean().unstack()

plt.figure(figsize=(10, 6))
sns.heatmap(state_season, annot=True, fmt=".2f", cmap='YlGnBu')
plt.title('Average Crop Yield (Tonnes/Ha) by State and Season')
plt.xlabel('Season')
plt.ylabel('State')
plt.tight_layout()
plt.savefig('q8_regional_consistency.png')
plt.show()