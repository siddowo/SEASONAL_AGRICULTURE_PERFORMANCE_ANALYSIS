import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('seasonal_agriculture_performance_dataset.csv')

# Average Revenue, Total Cost, and Profit by Season
econ_summary = df.groupby('Season')[['Revenue_INR', 'Total_Cost_INR', 'Profit_INR']].mean().reset_index()

econ_summary.plot(x='Season', kind='bar', figsize=(10, 6), color=['#2ca02c', '#d62728', '#1f77b4'])
plt.title('Economic Performance by Season (INR)')
plt.ylabel('Amount in INR')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig('q7_economic_outcomes.png')
plt.show()