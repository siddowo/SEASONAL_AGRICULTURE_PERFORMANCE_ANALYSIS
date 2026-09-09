import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('seasonal_agriculture_performance_dataset.csv')

# Correlation matrix between key variables
corr_cols = ['Rainfall_mm', 'Humidity_pct', 'Disease_Pest_Risk_pct', 'Yield_Tonnes_Ha', 'Water_Used_m3', 'Profit_INR']
corr_matrix = df[corr_cols].corr()

plt.figure(figsize=(8, 6))
sns.heatmap(corr_matrix, annot=True, fmt=".2f", cmap='coolwarm', vmin=-1, vmax=1)
plt.title('Correlation Analysis of Key Performance Metrics')
plt.tight_layout()
plt.savefig('q10_derived_insights.png')
plt.show()