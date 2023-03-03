import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Question 37
df = pd.read_excel('Ch08/Ch08/Excel/Fertility_and_life_expectancy_2014.xlsx', engine='openpyxl')

print(df.head())

plt.scatter(df['Fertility'], df['Life_expectancy'])
plt.title('Fertility vs. Life Expectancy')
plt.xlabel('Fertility rate (births per woman)')
plt.ylabel('Life Expectancy (years)')
plt.show()

r = np.corrcoef(df['Fertility'], df['Life_expectancy'])[0, 1]
a = df['Life_expectancy'].std()/df['Fertility'].std() * r
b = df['Life_expectancy'].mean() - a * df['Fertility'].mean()

print(f'ŷ = {b} + {a}x')
print(f'R-squared: {r**2}')

#Create a residual plot
df['residuals'] = df['Life_expectancy'] - (a * df['Fertility'] + b)
plt.scatter(df['Fertility'], df['residuals'])
plt.title('Residuals vs. Fertility')
plt.xlabel('Fertility Rate (births per woman)')
plt.ylabel('Residuals (years)')
plt.show()