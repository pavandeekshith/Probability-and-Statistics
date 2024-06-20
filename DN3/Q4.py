# The player who serves first wins a higher percentage of aces than the player who serves second.

import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("FrenchOpen-women-2013.csv")

# Calculate the percentage of aces won on first serve and second serve for each player
p1_first_serve_ace_pct = df['ACE.1'][df['FSW.1']>0].sum() / df['FSW.1'].sum()
p1_second_serve_ace_pct = df['ACE.1'][df['SSW.1']>0].sum() / df['SSW.1'].sum()
p2_first_serve_ace_pct = df['ACE.2'][df['FSW.2']>0].sum() / df['FSW.2'].sum()
p2_second_serve_ace_pct = df['ACE.2'][df['SSW.2']>0].sum() / df['SSW.2'].sum()

# Create a bar chart
plt.figure(figsize=(10,5))
labels = ['Player 1 First Serve Ace', 'Player 1 Second Serve Ace', 'Player 2 First Serve Ace', 'Player 2 Second Serve Ace']
sizes = [p1_first_serve_ace_pct.mean(), p1_second_serve_ace_pct.mean(), p2_first_serve_ace_pct.mean(), p2_second_serve_ace_pct.mean()]
plt.bar(labels, sizes)
plt.title('Mean Percentage of Aces Won on First Serve and Second Serve')
plt.ylabel('Percentage')
plt.show()