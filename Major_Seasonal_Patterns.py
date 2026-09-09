import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('seasonal_agriculture_performance_dataset.csv')

# Group by season for environmental trends
patterns = df.groupby('Season')[['Rainfall_mm', 'Avg_Temperature_C', 'Humidity_pct', 'Sunlight_Hours_Day']].mean().reset_index()

# Plot major seasonal patterns
fig, axes = plt.subplots(2, 2, figsize=(12, 8))
sns.barplot(data=patterns, x='Season', y='Rainfall_mm', ax=axes[0, 0], palette='Blues_d')
axes[0, 0].set_title('Mean Rainfall (mm)')

sns.barplot(data=patterns, x='Season', y='Avg_Temperature_C', ax=axes[0, 1], palette='Oranges_d')
axes[0, 1].set_title('Mean Temperature (°C)')

sns.barplot(data=patterns, x='Season', y='Humidity_pct', ax=axes[1, 0], palette='Purples_d')
axes[1, 0].set_title('Mean Humidity (%)')

sns.barplot(data=patterns, x='Season', y='Sunlight_Hours_Day', ax=axes[1, 1], palette='YlOrBr')
axes[1, 1].set_title('Mean Sunlight Hours/Day')

plt.tight_layout()
plt.savefig('q2_seasonal_patterns.png')
plt.show()