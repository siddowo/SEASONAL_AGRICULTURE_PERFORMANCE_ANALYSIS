import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('seasonal_agriculture_performance_dataset.csv')

# Water usage and fertilizer usage across seasons
resource_df = df.groupby('Season')[['Water_Used_m3', 'Fertilizer_kg_ha']].mean().reset_index()

fig, ax1 = plt.subplots(figsize=(9, 5))
sns.barplot(data=resource_df, x='Season', y='Water_Used_m3', palette='coolwarm', ax=ax1)
plt.title('Average Water Volume Used Across Seasons (m³)')
plt.ylabel('Water Used (m³)')
plt.tight_layout()
plt.savefig('q5_resource_usage.png')
plt.show()