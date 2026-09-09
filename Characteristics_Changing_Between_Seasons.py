import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('seasonal_agriculture_performance_dataset.csv')

# Compare Soil Moisture vs Pest Risk across seasons
char_df = df.groupby('Season')[['Soil_Moisture_pct', 'Disease_Pest_Risk_pct']].mean().reset_index()

fig, ax1 = plt.subplots(figsize=(9, 5))
sns.lineplot(data=char_df, x='Season', y='Soil_Moisture_pct', marker='o', color='blue', label='Soil Moisture (%)', ax=ax1)
ax2 = ax1.twinx()
sns.lineplot(data=char_df, x='Season', y='Disease_Pest_Risk_pct', marker='s', color='red', label='Pest Risk (%)', ax=ax2)

ax1.set_ylabel('Soil Moisture (%)', color='blue')
ax2.set_ylabel('Disease Pest Risk (%)', color='red')
plt.title('Seasonal Shifts in Soil Moisture and Pest Risk')
plt.tight_layout()
plt.savefig('q3_changing_characteristics.png')
plt.show()