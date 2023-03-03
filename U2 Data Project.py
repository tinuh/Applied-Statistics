import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

# read the csv file into a dataframe
df = pd.read_csv('rotten_tomatoes_movies.csv', engine='python')

print(df.head())

# fitler out movies wihout a numeric rating
df.dropna(subset=['tomatometer_rating', 'audience_rating', 'actors'], inplace=True)

# get data frame of movies with Timmothée Chalamet and Tom Holland
df_chalamet = df[df['actors'].str.contains('Chalamet')]
df_tom = df[df['actors'].str.contains('Tom Holland')]

# create a histogram of tomato meter ratings for Timmothée Chalamet movies
plt.hist(df_chalamet['tomatometer_rating'], bins=10)
plt.title('Tomatometer Rating (R-rated movies)')
plt.xlabel('Rating')
plt.ylabel('Number of Movies')
plt.show()

# create a scatter plot of tomato meter ratings vs. audience ratings for Timmothée Chalamet movies
plt.scatter(df_chalamet['tomatometer_rating'], df_chalamet['audience_rating'], s=8)
plt.xlabel('Tomatometer Rating')
plt.ylabel('Audience Rating')
plt.title('Tomatometer Rating vs. Audience Rating (R-rated movies)')

r = np.corrcoef(df_chalamet['tomatometer_rating'], df_chalamet['audience_rating'])[0, 1]
a = df_chalamet['audience_rating'].std()/df_chalamet['tomatometer_rating'].std() * r
b = df_chalamet['audience_rating'].mean() - a * df_chalamet['tomatometer_rating'].mean()

print(f'R-squared: {r**2}')
print(f'y = {b} + {a}x')

# plot the regression line
x = df_chalamet['tomatometer_rating']
y = a * x + b
plt.plot(x, y, color='red')
plt.show()

# create a residual plot
df_chalamet['residuals'] = df_chalamet['audience_rating'] - (a * df_chalamet['tomatometer_rating'] + b)
plt.scatter(df_chalamet['tomatometer_rating'], df_chalamet['residuals'], s=8)
plt.title('Residuals vs. Tomatometer Rating (R-rated movies)')
plt.xlabel('Tomatometer Rating')
plt.ylabel('Residuals (pounds)')
plt.show()

#create a historgram of tomato meter ratings for Tom Holland movies
plt.hist(df_tom['tomatometer_rating'], bins=10)
plt.title('Tomatometer Rating (Tom Holland movies)')
plt.xlabel('Rating')
plt.ylabel('Number of Movies')
plt.show()

# create a scatter plot of tomato meter ratings vs. audience ratings for Tom Holland movies
plt.scatter(df_tom['tomatometer_rating'], df_tom['audience_rating'], s=8)
plt.xlabel('Tomatometer Rating')
plt.ylabel('Audience Rating')
plt.title('Tomatometer Rating vs. Audience Rating (Tom Holland movies)')

r = np.corrcoef(df_tom['tomatometer_rating'], df_tom['audience_rating'])[0, 1]
a = df_tom['audience_rating'].std()/df_tom['tomatometer_rating'].std() * r
b = df_tom['audience_rating'].mean() - a * df_tom['tomatometer_rating'].mean()

print(f'R-squared {r**2}')
print(f'y = {b} + {a}x')

# plot the regression line for Tom Holland movies
x = df_tom['tomatometer_rating']
y = a * x + b
plt.plot(x, y, color='red')
plt.show()

# create a residual plot for Tom Holland movies
df_tom['residuals'] = df_tom['audience_rating'] - (a * df_tom['tomatometer_rating'] + b)
plt.scatter(df_tom['tomatometer_rating'], df_tom['residuals'], s=8)
plt.title('Residuals vs. Tomatometer Rating (PG-rated movies)')
plt.xlabel('Tomatometer Rating')
plt.ylabel('Residuals (pounds)')
plt.show()
