# Players who win the first set are more likely to win the match

import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("Wimbledon-men-2013.csv")

# Count the number of matches won and lost based on who won the first set
first_set_winners = df[df['ST1.1'] > df['ST1.2']]
first_set_losers = df[df['ST1.1'] < df['ST1.2']]
num_matches = len(first_set_winners) + len(first_set_losers)

# Calculate the percentage of matches won by first set winners and first set losers
pct_first_set_winners = len(first_set_winners) / num_matches * 100
pct_first_set_losers = len(first_set_losers) / num_matches * 100

# Create a bar chart to display the results
plt.bar(['First set winners', 'First set losers'], [pct_first_set_winners, pct_first_set_losers])
plt.ylabel('Percentage of matches won')
plt.title('Effect of winning the first set on match outcomes')
plt.show()