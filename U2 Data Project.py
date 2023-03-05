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

# describe the tamatometer ratings for Timmothée Chalamet and Tom Holland movies
print(df_chalamet['tomatometer_rating'].describe())
print(df_tom['tomatometer_rating'].describe())

#create a boxplot of tomato meter ratings for Timmothée Chalamet and Tom Holland movies
plt.boxplot([df_chalamet['tomatometer_rating'], df_tom['tomatometer_rating']], labels=['Timmothée Chalamet', 'Tom Holland'])
plt.title('Tomatometer Rating (Timmothée Chalamet vs. Tom Holland movies)')
plt.ylabel('Rating')
plt.show()

# create a histogram of tomato meter ratings for Timmothée Chalamet movies
plt.hist(df_chalamet['tomatometer_rating'], bins=8)
plt.title('Tomatometer Rating (Timmothée Chalamet movies)')
plt.xlabel('Rating')
plt.ylabel('Number of Movies')
plt.show()

# create a scatter plot of tomato meter ratings vs. audience ratings for Timmothée Chalamet movies
plt.scatter(df_chalamet['tomatometer_rating'], df_chalamet['audience_rating'], s=8)
plt.xlabel('Tomatometer Rating')
plt.ylabel('Audience Rating')
plt.title('Tomatometer Rating vs. Audience Rating (Timmothée Chalamet movies)')

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

# total sum of squares for Timmothée Chalamet movies
tss = ((df_chalamet['audience_rating'] - df_chalamet['audience_rating'].mean())**2).sum()
print(f'TSS: {tss}')

# residual sum of squares for Timmothée Chalamet movies
rss = ((df_chalamet['audience_rating'] - y)**2).sum()
print(f'RSS: {rss}')

# create a residual plot
df_chalamet['residuals'] = df_chalamet['audience_rating'] - (a * df_chalamet['tomatometer_rating'] + b)
plt.scatter(df_chalamet['tomatometer_rating'], df_chalamet['residuals'], s=8)
plt.title('Residuals vs. Tomatometer Rating (Timmothée Chalamet movies)')
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

# total sum of squares for Tom Holland movies
tss = ((df_tom['audience_rating'] - df_tom['audience_rating'].mean())**2).sum()
print(f'TSS: {tss}')

# residual sum of squares for Tom Holland movies
rss = ((df_tom['audience_rating'] - y)**2).sum()
print(f'RSS: {rss}')

# create a residual plot for Tom Holland movies
df_tom['residuals'] = df_tom['audience_rating'] - (a * df_tom['tomatometer_rating'] + b)
plt.scatter(df_tom['tomatometer_rating'], df_tom['residuals'], s=8)
plt.title('Residuals vs. Tomatometer Rating (Tom Holland movies)')
plt.xlabel('Tomatometer Rating')
plt.ylabel('Residuals (pounds)')
plt.show()
