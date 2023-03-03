import pandas as pd
from matplotlib import pyplot as plt
from scipy import stats
import seaborn as sns

# Read in the data
df = pd.read_excel('yelp data.xlsx', engine='openpyxl')

# Print the first 5 rows of the dataframe
print(df.head())

# split the data into two groups based on the value of the is_open column
openbiz = df.query('is_open == 1')
closedbiz = df.query('is_open == 0')

fig, ax = plt.subplots()
ax.boxplot([openbiz['stars'], closedbiz['stars']], labels=['Open', 'Closed'])

# label axes
ax.set_xlabel('Status') # set a label for the x (horizontal) axis
ax.set_ylabel('Rating') # set a label for the y (vertical) axis

plt.show()

print(openbiz['stars'].describe())
fig, ax = plt.subplots()
ax.hist(openbiz['stars'], bins=8)

# label axes
ax.set_title('Ratings of Open Businesses') # set the title
ax.set_xlabel('Rating') # set a label for the x (horizontal) axis
ax.set_ylabel('Frequency') # set a label for the y (vertical) axis

plt.show()

print(closedbiz['stars'].describe())
closedbizNoOutliers = closedbiz.query('stars != 1')
print(closedbizNoOutliers['stars'].describe())
fig, ax = plt.subplots()
ax.hist(closedbiz['stars'], bins=8)

# label axes
ax.set_title('Ratings of Closed Businesses') # set the title
ax.set_xlabel('Rating') # set a label for the x (horizontal) axis
ax.set_ylabel('Frequency') # set a label for the y (vertical) axis

plt.show()

#standardize the data using the z-score
df['z_stars'] = (df['stars'] - df['stars'].mean())/df['stars'].std()

# split the data into two groups based on the value of the is_open column
openbiz = df.query('is_open == 1')
closedbiz = df.query('is_open == 0')

print(openbiz['z_stars'].describe())
print(closedbiz['z_stars'].describe())

# plot the probability plots
res = stats.probplot(openbiz['z_stars'], plot=plt, dist='norm', fit=stats.norm)
# label axes
ax.set_xlabel('Theoretical Quantiles') # set a label for the x (horizontal) axis
ax.set_ylabel('Sample Quantiles') # set a label for the y (vertical) axis
ax.set_title('Probability Plot of Ratings of Open Businesses') # set the title
plt.show()

res = stats.probplot(closedbiz['z_stars'], plot=plt, dist='norm', fit=stats.norm)
# label axes
ax.set_xlabel('Theoretical Quantiles') # set a label for the x (horizontal) axis
ax.set_ylabel('Sample Quantiles') # set a label for the y (vertical) axis
ax.set_title('Probability Plot of Ratings of Closed Businesses') # set the title
plt.show()

fig, ax = plt.subplots()
ax.boxplot([openbiz['z_stars'], closedbiz['z_stars']], labels=['Open', 'Closed'])
plt.show()