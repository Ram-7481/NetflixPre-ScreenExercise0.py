import os
print(os.getcwd())
print(os.listdir())

import pandas as pd

file_path = r"C:\Users\sunny\Desktop\Data File.xlsx"

netflix_df = pd.read_excel(file_path, sheet_name="NFLX Top 10")
imdb_df = pd.read_excel(file_path, sheet_name="IMDB Rating")

print(netflix_df.head())
print(imdb_df.head())

## Find the most recent week
latest_week = netflix_df["week"].max()

## Filter Netflix records for the most recent week
latest_data = netflix_df[netflix_df["week"] == latest_week]

print(latest_data)

## Merge latest Netflix data with IMDb ratings using title
merged_data = latest_data.merge(
    imdb_df,
    left_on="show_title",
    right_on="title"
)

## Display the most recent week in Month Day, Year format
print("Most recent week:", latest_week.strftime("%B %d, %Y"))

## Filter out unrated/missing IMDb ratings
rated_data = merged_data[merged_data["rating"] > 0]

## Identify the title with the lowest valid IMDb rating
lowest_title = rated_data.loc[rated_data["rating"].idxmin()]

## Display the final result
print("Title:", lowest_title["show_title"])
print("IMDb Rating:", lowest_title["rating"])
print("Weekly Rank:", lowest_title["weekly_rank"])