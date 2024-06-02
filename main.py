import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset

ipl_data = pd.read_csv("deliveries.csv")
ipl_data = pd.read_csv("matches.csv")

# Display the first few rows of the dataset
print(ipl_data.head())

# Basic information about the dataset
print(ipl_data.info())

# Summary statistics of the dataset
print(ipl_data.describe())

# Checking for missing values
print(ipl_data.isnull().sum())

# Data visualization
# Distribution of matches won by each team
plt.figure(figsize=(12, 6))
sns.countplot(x='winner', data=ipl_data, order=ipl_data['winner'].value_counts().index)
plt.xticks(rotation=90)
plt.title('Number of Matches Won by Each Team')
plt.xlabel('Team')
plt.ylabel('Number of Wins')
plt.show()

# Distribution of player of the match awards
plt.figure(figsize=(12, 6))
top_players = ipl_data['player_of_match'].value_counts().head(10)
sns.barplot(x=top_players.index, y=top_players.values)
plt.xticks(rotation=90)
plt.title('Top 10 Players with Most Player of the Match Awards')
plt.xlabel('Player')
plt.ylabel('Number of Awards')
plt.show()

# Factors contributing to win or loss of a team
# Example: Impact of toss decision on match outcome
plt.figure(figsize=(12, 6))
sns.countplot(x='toss_decision', hue='winner', data=ipl_data)
plt.title('Impact of Toss Decision on Match Outcome')
plt.xlabel('Toss Decision')
plt.ylabel('Number of Matches Won')
plt.show()

# Example: Impact of venue on match outcome
plt.figure(figsize=(12, 6))
sns.countplot(x='venue', hue='winner', data=ipl_data, order=ipl_data['venue'].value_counts().index)
plt.xticks(rotation=90)
plt.title('Impact of Venue on Match Outcome')
plt.xlabel('Venue')
plt.ylabel('Number of Matches Won')
plt.show()

# Suggesting teams or players a company should endorse
# Based on top players and successful teams
top_teams = ipl_data['winner'].value_counts().head(3)
print("Top 3 Teams to Endorse:", top_teams.index.tolist())

top_players = ipl_data['player_of_match'].value_counts().head(3)
print("Top 3 Players to Endorse:", top_players.index.tolist())
