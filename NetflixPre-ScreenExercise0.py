import os
print(os.getcwd())
print(os.listdir())

import pandas as pd

df = pd.read_excel(r"C:\Users\sunny\Desktop\Data File.xlsx")

print(df.head())

print("Rows and Columns:", df.shape)
print("\nFirst 5 Rows:")
print(df.head())
print("\nLast 5 Rows:")
print(df.tail())
print("\nColumns:")
print(df.columns.tolist())
print("\nData Information:")
df.info()

missing_values = df.isnull().sum()
duplicates = df.duplicated().sum()

print(missing_values)
print("Duplicate Rows =", duplicates)

print("\nStatistics:")
print(df.describe())

print("\nUnique Values:")
print(df.nunique())

# Most Recent Week
latest_week = df['week'].max()

print("Most Recent Week:")
print(latest_week)

# Data for Most Recent Week
latest_data = df[df['week'] == latest_week]

print("\nRows in Latest Week:")
print(latest_data.shape)

print("\nFirst 5 Rows:")
print(latest_data.head())

# English Titles Only
english_data = latest_data[
    (latest_data['category'] == 'Films (English)') |
    (latest_data['category'] == 'TV (English)')
]

print("English Titles Rows:")
print(english_data.shape)

print("\nFirst 5 Rows:")
print(english_data.head())

# Highest cumulative weeks in latest week
top_title = english_data.loc[
    english_data['cumulative_weeks_in_top_10'].idxmax()
]

print("Top Title:")
print(top_title[['show_title', 'cumulative_weeks_in_top_10']])

# Title name store karo
title_name = top_title['show_title']

# Same title ka poora data
title_data = df[
    df['show_title'].str.contains('Stranger Things', na=False)
]

# Outage week remove karo
title_data = title_data[title_data['week'] != '2022-05-22']

print("Rows after removing outage week:")
print(title_data.shape)

print("\nFirst 5 Rows:")
print(title_data.head())

# Average weekly hours viewed
avg_hours = title_data['weekly_hours_viewed'].mean()

print("Title Name:", title_name)
print("Average Weekly Hours Viewed:", round(avg_hours, 2))

print("Total Rows:", len(title_data))
print(title_data[['week','weekly_hours_viewed']].sort_values('week'))

print(title_data.columns)

print(
    title_data.sort_values(
        'cumulative_weeks_in_top_10',
        ascending=False
    )[
        ['show_title',
         'season_title',
         'cumulative_weeks_in_top_10']
    ].head(10)
)

## Ranking Analysis:
## Top titles were ranked based on cumulative weeks in Top 10
top_10_titles = (
    english_data
    .sort_values('cumulative_weeks_in_top_10', ascending=False)
    [['show_title', 'season_title', 'cumulative_weeks_in_top_10']]
    .drop_duplicates(subset='show_title')
    .head(10)
)

print(top_10_titles)

# Average weekly hours viewed for title with highest cumulative weeks in Top 10

avg_hours = title_data['weekly_hours_viewed'].mean()

print("Top Title:", title_name)
print("Average Weekly Hours Viewed:", round(avg_hours, 2))

print("Total Rows:", len(title_data))

print(
    title_data[
        ['week','weekly_hours_viewed']
    ].sort_values('week')
)

## Key Finding:
## Stranger Things recorded the highest cumulative presence in Top 10 rankings.
cumulative_weeks = top_title['cumulative_weeks_in_top_10']
print("Cumulative Weeks in Top 10:", cumulative_weeks)

## Insight:
## Stranger Things has the highest cumulative weeks in Top 10.
## It maintained strong audience engagement across multiple weeks.
print("\nInsight:")
print("Stranger Things has the highest cumulative weeks in Top 10 with", cumulative_weeks, "weeks.")
print("It maintained strong audience engagement across multiple weeks.")
print("Average Weekly Hours Viewed:", round(avg_hours, 2))

print("\nFinal Answer:")
print("English Title: Stranger Things")
print("Cumulative Weeks in Top 10:", cumulative_weeks)
print("Average Weekly Hours Viewed:", f"{avg_hours:,.0f}")