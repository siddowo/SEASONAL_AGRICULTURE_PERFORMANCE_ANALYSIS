import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv('seasonal_agriculture_performance_dataset.csv')

# Aggregate mean yield and production by season
seasonal_perf = df.groupby('Season')[['Yield_Tonnes_Ha', 'Production_Tonnes']].mean().reset_index()

# Plotting performance across seasons
plt.figure(figsize=(10, 5))
sns.barplot(data=seasonal_perf, x='Season', y='Yield_Tonnes_Ha', palette='viridis')
plt.title('Average Agricultural Yield Across Seasons (Tonnes/Ha)')
plt.xlabel('Season')
plt.ylabel('Yield (Tonnes/Ha)')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig('q1_seasonal_performance.png')
plt.show()