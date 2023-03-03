import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

#Question 63
df = pd.read_excel('Ch07/Ch07/Excel/Womens_Heptathlon_2016.xlsx', engine='openpyxl')

plt.scatter(df['800m'], df['LongJump'])
plt.title('800m vs. Long Jump')
plt.xlabel('800m (seconds)')
plt.ylabel('Long Jump (meters)')
plt.show()

a = df['LongJump'].std()/df['800m'].std() * np.corrcoef(df['800m'], df['LongJump'])[0, 1]
b = df['LongJump'].mean() - a * df['800m'].mean()

print(f'y = {b} + {a}x')

#create a residual plot
df['residuals'] = df['LongJump'] - (a * df['800m'] + b)
plt.scatter(df['800m'], df['residuals'])
plt.title('Residuals vs. 800m')
plt.xlabel('800m (seconds)')
plt.ylabel('Residuals (meters)')
plt.show()

print(f'Residual Standard Deviation: {df["residuals"].std()}')
print(f'Standard Deviation of Long Jump: {df["LongJump"].std()}')