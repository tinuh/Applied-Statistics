import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

# read the excel file into a dataframe
df = pd.read_excel('Unit_three_takehome_data.xlsx', engine='openpyxl')

# create a column of random values between 0 and 1
df['random'] = np.random.uniform(0, 1, len(df))

# sort all columns by the random column
df = df.sort_values('random')

# split the dataframe into two dataframes
df_a = df.iloc[:len(df)//2]
df_b = df.iloc[len(df)//2:]

# create a histogram of the A improvement column
plt.hist(df_a['A improvement'])
plt.title('A improvement')
plt.xlabel('Improvement')
plt.ylabel('Count')
plt.show()

# create a histogram of the B improvement column
plt.hist(df_b['B improvement'])
plt.title('B improvement')
plt.xlabel('Improvement')
plt.ylabel('Count')
plt.show()

# print out summary statistics
print(f'A Improvement \n {df_a["A improvement"].describe()}')
print(f'B Improvement \n {df_b["A improvement"].describe()}')

# create a boxplot of the A improvement and B improvement columns
plt.boxplot([df_a['A improvement'], df_b['B improvement']], labels=['A', 'B'])
plt.title('A improvement vs. B improvement')
plt.ylabel('Improvement')
plt.show()

# split df based on gender
df_m = df[df['Gender'].str.contains("Male")]
df_f = df[df['Gender'].str.contains("Female")]

df_m['random'] = np.random.uniform(0, 1, len(df_m))
df_m = df_m.sort_values('random')

df_f['random'] = np.random.uniform(0, 1, len(df_f))
df_f = df_f.sort_values('random')

df_m_a = df_m.iloc[:len(df_m)//2]
df_m_b = df_m.iloc[len(df_m)//2:]

df_f_a = df_f.iloc[:len(df_f)//2]
df_f_b = df_f.iloc[len(df_f)//2:]

# make histograms for each dataframe
plt.hist(df_m_a['A improvement'])
plt.title('Improvement in Cholesterol Levels in Males with Drug A')
plt.xlabel('Improvement')
plt.ylabel('Count')
plt.show()

plt.hist(df_m_b['B improvement'])
plt.title('Improvement in Cholesterol Levels in Males with Drug B')
plt.xlabel('Improvement')
plt.ylabel('Count')
plt.show()

plt.hist(df_f_a['A improvement'])
plt.title('Improvement in Cholesterol Levels in Females with Drug A')
plt.xlabel('Improvement')
plt.ylabel('Count')
plt.show()

plt.hist(df_f_b['B improvement'])
plt.title('Improvement in Cholesterol Levels in Females with Drug B')
plt.xlabel('Improvement')
plt.ylabel('Count')
plt.show()

# print out summary statistics for each dataframe
print(f'A Improvement Males \n {df_m_a["A improvement"].describe()}')
print(f'B Improvement Males \n {df_m_b["B improvement"].describe()}')
print(f'A Improvement Females \n {df_f_a["A improvement"].describe()}')
print(f'B Improvement Females \n {df_f_b["B improvement"].describe()}')

# make a boxplot for Males
plt.boxplot([df_m_a['A improvement'], df_m_b['B improvement']], labels=['Drug A', 'Drug B'])
plt.title('Improvements in Cholesterol Levels in Males')
plt.ylabel('Improvement')
plt.show()

# make a boxplot for Females
plt.boxplot([df_f_a['A improvement'], df_f_b['B improvement']], labels=['Drug A', 'Drug B'])
plt.title('Improvements in Cholesterol Levels in Females')
plt.ylabel('Improvement')
plt.show()