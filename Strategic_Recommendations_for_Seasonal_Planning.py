import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('seasonal_agriculture_performance_dataset.csv')

# Profitability by Irrigation Method in Zaid Season
zaid_df = df[df['Season'] == 'Zaid']
zaid_irrigation = zaid_df.groupby('Irrigation_Method')['Profit_INR'].mean().reset_index()

plt.figure(figsize=(9, 5))
sns.barplot(data=zaid_irrigation, x='Irrigation_Method', y='Profit_INR', palette='magma')
plt.axhline(0, color='black', linewidth=1)
plt.title('Impact of Irrigation Method on Zaid Season Profitability (INR)')
plt.xlabel('Irrigation Method')
plt.ylabel('Mean Profit (INR)')
plt.tight_layout()
plt.savefig('q12_seasonal_planning.png')
plt.show()