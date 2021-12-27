import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("crypto.csv")
df = df.sort_values("current_price")


"""
Box plot for current prices
"""

plt.boxplot(df['current_price'][:50])
plt.title("Box plot")
plt.show()
"""
Pie chart for current prices
"""
data = df['current_price'][:15]
plt.pie(data, labels=df['id'][:15])
plt.title("Pie chart for prices")
plt.legend(loc='upper left')
plt.show()
"""
Scatter plot for x "id" against y "current price"
"""
df[:10].plot.scatter(x='id', y='current_price', colormap='viridis')
plt.title("scatter plot")
plt.show()
"""
Bar plot for x "id" against y "current price
"""
sns.barplot(x='id', y='current_price', data=df[:10])
plt.title("bar chart of price vs id")
plt.show()
