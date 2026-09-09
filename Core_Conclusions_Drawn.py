import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('seasonal_agriculture_performance_dataset.csv')

# Proportion of profitable farms by season
df['Is_Profitable'] = df['Profit_INR'] > 0
profit_rates = df.groupby('Season')['Is_Profitable'].mean() * 100

plt.figure(figsize=(8, 5))
profit_rates.plot(kind='pie', autopct='%1.1f%%', colors=['#66b3ff','#99ff99','#ffcc99'], startangle=90)
plt.title('Percentage of Profitable Farms by Season')
plt.ylabel('')
plt.tight_layout()
plt.savefig('q11_conclusions.png')
plt.show()