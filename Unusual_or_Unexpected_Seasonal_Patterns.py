import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('seasonal_agriculture_performance_dataset.csv')

# Water Efficiency (t per 1000m3) vs Profitability by Season
plt.figure(figsize=(9, 5))
sns.boxplot(data=df, x='Season', y='Water_Efficiency_t_per_1000m3', palette='Set3')
plt.title('Water Use Efficiency (Tonnes per 1,000 m³) Across Seasons')
plt.ylabel('Water Efficiency (t / 1,000 m³)')
plt.tight_layout()
plt.savefig('q9_unexpected_patterns.png')
plt.show()