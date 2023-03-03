import pandas as pd
from matplotlib import pyplot as plt

#Question 33
df = pd.read_excel('Ch04/Ch04/Excel/Industrial_experimentv2.xlsx',engine='openpyxl')

print(df.head()) # See the top 5 rows of the dataframe

fast = df.query('Speed == "Fast"')
slow = df.query('Speed == "Slow"')

fig, ax = plt.subplots()
ax.boxplot([fast['Distance'], slow['Distance']], labels=['Fast', 'Slow'])
#ax.boxplot(fast['Distance'])

# label axes
ax.set_xlabel('Speed of Drill') # set a label for the x (horizontal) axis
ax.set_ylabel('Distance (in.)') # set a label for the y (vertical) axis

plt.show()

#Qeustion 34
df = pd.read_excel('Ch04/Ch04/Excel/Cholesterol.xlsx',engine='openpyxl')

fig, ax = plt.subplots()
ax.boxplot([df['Smokers'], df['Ex-Smokers']], labels=['Smokers', 'Ex-Smokers'])

# label axes
ax.set_xlabel('Type') # set a label for the x (horizontal) axis
ax.set_ylabel('Chrolesterol Level') # set a label for the y (vertical) axis

plt.show()

print(df['Smokers'].describe())

fig, ax = plt.subplots()
ax.hist(df['Smokers'], bins=15)

# label axes
ax.set_title('Chrolesterol Levels in Smokers') # set the title
ax.set_xlabel('Chrolesterol Level') # set a label for the x (horizontal) axis
ax.set_ylabel('Frequency') # set a label for the y (vertical) axis
plt.show()

print(df['Ex-Smokers'].describe())

fig, ax = plt.subplots()
ax.hist(df['Ex-Smokers'], bins=15)

# label axes
ax.set_title('Chrolesterol Levels in Ex-Smokers') # set the title
ax.set_xlabel('Chrolesterol Level') # set a label for the x (horizontal) axis
ax.set_ylabel('Frequency') # set a label for the y (vertical) axis
plt.show()