-----------------Pandas-----------
# Shape
df.shape
# show columns
df.columns
# Count what is in columns
df.count()
# Change NaN (not a number) to '0'
df.fillna(0, inplace=True) # inplace - saves that to df
# check if there are still any NaN
df.isna().values.any()
# Chart
import matplotlib.pyplot as plt
plt.plot(pivoted_df.index, pivoted_df.java)
----------
# Multiple charts
plt.figure(figsize=(16,10))
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)

plt.xlabel('Date', fontsize=14)
plt.ylabel('Number of posts', fontsize=14)
plt.ylim(0, 35000)
for column in pivoted_df.columns:
  plt.plot(pivoted_df.index, pivoted_df[column],
            linewidth=3, label=pivoted_df.column.name)
plt.legend(fontsize=16)

# Smoothing out chart
roll_df = pivoted_df.rolling(window=6).mean() # this line goes at the top of "Multiple charts" paragraph
# And roll_df is used further down the line
------

df.loc[df['Type 1'] == 'Fire']      # look up rows that in "Type 1" has value == "Fire"
df.describe()  # Detailed precise description in digits
df.sort_values('Name') # Sorting in alphabetical order
df.sort_values(['Name', 'HP'], ascending=[1,0]) # Name-ascending, HP- discending

# Creating new column- that is a total- of columns I specified
df['Total'] = df['HP'] + df['Attack'] + df['Defense'] + df['Sp. Atk'] + df['Sp. Def'] + df['Speed']
# same, where axis- is horisontal
df['Total'] = df.iloc[:, 4:10].sum(axis=1)
# Droping a column
df = df.drop(columns=['Total'])
# Changing the columns order; [cols[-1]] is last column wich we move to the front
cols = list(df.columns)
df = df[cols[:4] + [cols[-1]] + cols[4:12]]
# saving db
df.to_csv('modified.csv')
df.to_excel('modified.xlsx', index=False) # index will not be saved
df.to_csv('modified.txt', index=False, sep='\t') # separator of TAB is needed for txt file
# Filtering Data: printing 2 types- found in 2 columns (entire row)
df.loc[(df['Type 1'] == 'Grass') & (df['Type 2'] == 'Poison')]
# Printing one type OR the other (entire row)
df.loc[(df['Type 1'] == 'Grass') | (df['Type 2'] == 'Poison')] # where "|" is "OR"

df.loc[(df['Type 1'] == 'Grass') | (df['Type 2'] == 'Poison') & (df['HP']>70)]

# Re_setting index
new_df = df.reset_index() # saves old index as a new column
new_df = df.reset_index(drop=True) # drops old reset_index
new_df = df.reset_index(drop=True, inplace=True) # inplace=True - saves db
# Other conditions
df.loc[df['Name'].str.contains('Mega')] # Got all rows for column "Name" that contain "Mega"
df.loc[~df['Name'].str.contains('Mega')] # Reverse. "~" means "not"
# Grab "Fire" or "Grass" in column "Type 1"
import re
df.loc[df["Type 1"].str.contains('Fire|Grass', regex=True)]  # regex- "re"
df.loc[df["Type 1"].str.contains('fire|grass', flags=re.I, regex=True)] # "flags=re.I" means "ignore capitalization"
# "^pi[a-z]*" - Name starts with "^pi", then letter a-z, "*"- one ore more; without "^" we display "pi" found anywhere in Name
df.loc[df["Name"].str.contains('^pi[a-z]*', flags=re.I, regex=True)]

# Conditional changes
df.loc[df['Type 1'] == 'Fire', 'Type 1'] = "Flamer" # Changes "Fire" into "Flamer"
df.loc[df['Type 1'] == 'Fire', 'Legendary'] = "True" # will write "True" in column "Legendary" for all "Fire"

df.loc[df['Total'] > 500, ['Generation', 'Legendary']] = "TEST VALUE" # If "Total" > 500: "Generation" and "Legendary" are set to "TEST VALUE"
df.loc[df['Total'] > 500, ['Generation', 'Legendary']] = ['Test 1', 'Test 2'] # Setting "Generation" to 'Test 1' and "Legendary" to "Test 2"

# If does not work - re load df
df = pd.read_csv('modified.csv')
df
# Agregate statistics with "groupby"
df.groupby(['Type 1']).mean() # looking for average 'Type 1' with function "mean()"
df.groupby(['Type 1']).mean().sort_values('Defense', ascending=False) # Sorting "Defence", showing highest sort_values
df.groupby(['Type 1']).sum() # -in "Type 1"- inside every Name- values will be summed up

# Adding column that will count instances
df['count'] = 1
df.groupby(['Type 1']).count()['count'] # I group db by 'Type 1', and count each instances (of "count")

# WORKING WITH LARGE AMOUNT OF Data
# chunksize=5 -is 5 rows
new_df = pd.DataFrame(columns=df.columns) # Create new_df with same column's names as original df

for df in pd.read_csv('modified.csv', chunksize=5):
    results = df.groupby(['Type 1']).count() # Group by 'type 1' and get count of that, store it in 'results'
    # SAVING RESULTS IN NEW_DF
    df1 = pd.concat([new_df, results]) # results is stored in new_df, that has same columns as old df

# Change time format
df.DATE = pd.to_datetime(df['DATE'])

# Pivot db
pivoted_df = df.pivot(index="DATE", columns='TAG', values='POSTS')
# Number of unique colors
num_colors = df.name.nunique()
df['name'].nunique()

# Count transparent colors
trans = df.groupby('is_trans').count()
# Find first year release
sets.sort_values('year').head()
# displays info base on year
sets[sets['year'] == 1949]
# top 5 LEGO sets with the most number of parts.
sets.sort_values('num_parts', ascending=False).head(5)

# Group by year and count
num_sets_per_year = sets.groupby(sets['year']).count()

# agg()
themes_by_year = sets.groupby(sets['year']).agg({'theme_id':pd.Series.nunique})
themes_by_year.rename(columns={"themes_id": "nr_themes"}, inplace=True) # rename columns

# agg() and average number - using pd.Series.mean
parts_per_set = sets.groupby('year').agg({'num_parts': pd.Series.mean})

------
# plot on same axis
ax1 = plt.gca()
ax2 = ax1.twinx()
ax1.plot(num_sets_per_year.index[:-2], num_sets_per_year.set_num[:-2], color='g')
ax2.plot(themes_by_year.index[:-2], themes_by_year.theme_id[:-2], color='b')
ax1.set_xlabel('Year')
ax2.set_ylabel('Number of sets', color='g')
ax2.set_ylabel('Number of themes', color='b')
-----
# Scatter
plt.scatter(parts_per_set.index[:-2], parts_per_set.num_parts[:-2])

# Series -to- DataFrame
set_theme_count = pd.DataFrame({'id': set_theme_count.index, 'set_count': set_theme_count.values})

# Combining DataFrames base on a Key- names of 2 DataFrames + on='id'
merged_df = pd.merge(set_theme_count, themes, on='id')
# plot Bar
plt.bar(merged_df.name[:10], merged_df.set_count[:10])
