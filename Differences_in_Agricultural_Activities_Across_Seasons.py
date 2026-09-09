import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('seasonal_agriculture_performance_dataset.csv')

# Distribution of Irrigation Methods by Season
irrigation_ct = pd.crosstab(df['Season'], df['Irrigation_Method'])

irrigation_ct.plot(kind='bar', stacked=True, figsize=(10, 6), colormap='Set2')
plt.title('Irrigation Method Usage Across Seasons')
plt.xlabel('Season')
plt.ylabel('Number of Farms')
plt.legend(title='Irrigation Method')
plt.tight_layout()
plt.savefig('q4_activities_irrigation.png')
plt.show()