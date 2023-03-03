import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

#Question 5
df = pd.read_excel('Ch06/Ch06/Excel/Armspans.xlsx',engine='openpyxl')

print(df.head()) # See the top 5 rows of the dataframe

plt.scatter(df['Armspan_cm'], df['Height_cm'])
plt.title('Height vs. Armspan')
plt.xlabel('Armspan (cm)')
plt.ylabel('Height (cm)')

plt.show()

#Question 42
df = pd.read_excel('Ch06/Ch06/Excel/Vehicle_weights.xlsx',engine='openpyxl')

print(np.corrcoef(df['Static Weight'], df['Weight-in-Motion'])[0, 1])

df['Static Weight kg'] = df['Static Weight'] * 0.4545

print(np.corrcoef(df['Static Weight kg'], df['Weight-in-Motion'])[0, 1])

print(df.head()) # See the top 5 rows of the dataframe

plt.scatter(df['Static Weight'], df['Weight-in-Motion'])
plt.title('Weight-in-Motion vs. Static Weight')
plt.xlabel('Static Weight (1000s of lbs)')
plt.ylabel('Weight-in-Motion (1000s of lbs)')
plt.show()