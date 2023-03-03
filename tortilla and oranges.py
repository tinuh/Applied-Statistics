import pandas as pd
from matplotlib import pyplot as plt
from scipy import stats
import numpy as np

# read the excel file into a dataframe
df = pd.read_excel('tortillas and oranges.xlsx', engine='openpyxl')

# df['lb/fruit'] = 1/df['lb/fruit']

# # create a scatter plot
# plt.scatter(df['oranges/tree'], df['lb/fruit'])
# plt.xlabel('Oranges per Tree')
# plt.ylabel('Pounds for Fruit')
# plt.title('Oranges per Tree vs. Pounds for Fruit')

# r = np.corrcoef(df['oranges/tree'], df['lb/fruit'])[0, 1]
# a = df['lb/fruit'].std()/df['oranges/tree'].std() * r
# b = df['lb/fruit'].mean() - a * df['oranges/tree'].mean()

# print(f'R-squared: {r**2}')
# print(f'1/y = {b} + {a}x')

# # plot the regression line
# x = df['oranges/tree']
# y = a * x + b
# plt.plot(x, y, color='red')
# plt.show()

# create a residual plot
# df['residuals'] = df['lb/fruit'] - (a * df['oranges/tree'] + b)
# plt.scatter(df['oranges/tree'], df['residuals'])
# plt.title('Residuals vs. Oranges per Tree')
# plt.xlabel('Oranges per Tree')
# plt.ylabel('Residuals (pounds)')
# plt.show()

# 1/y
df['moisture'] = 1/df['moisture']

# create a scatter plot
plt.scatter(df['frying_time'], df['moisture'])
plt.xlabel('Frying Time (minutes)')
plt.ylabel('Moisture (%)')
plt.title('Frying Time vs. Moisture')

r = np.corrcoef(df['frying_time'], df['moisture'])[0, 1]
a = df['moisture'].std()/df['frying_time'].std() * r
b = df['moisture'].mean() - a * df['frying_time'].mean()

print(f'R-squared: {r**2}')
print(f'y = {b} + {a}x')

# plot the regression line
x = df['frying_time']
y = a * x + b
plt.plot(x, y, color='red')
plt.show()

# create a residual plot
df['residuals'] = df['moisture'] - (a * df['frying_time'] + b)
plt.scatter(df['frying_time'], df['residuals'])
plt.title('Residuals vs. Frying Time')
plt.xlabel('Frying Time (minutes)')
plt.ylabel('Residuals (%)')
plt.show()