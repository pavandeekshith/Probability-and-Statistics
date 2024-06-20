# Players who win a higher percentage of games on their opponent's serve also win a higher percentage of games on their own serve.
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("AusOpen-men-2013.csv")

# Calculate the percentage of games won on serve for each player
p1_serve_win_pct = (df['FNL1'] + df['FNL2']) / (df['FNL1'] + df['FNL2'] + df['FSP.1'] + df['SSP.1'])
p2_serve_win_pct = (df['WNR.2']) / (df['FNL1'] + df['FNL2'] + df['FSP.1'] + df['SSP.1'])

# Calculate the total games won by each player
p1_total_games_won = df['WNR.1'].sum()
p2_total_games_won = df['WNR.2'].sum()

# Calculate the percentage of games won on opponent's serve for each player
p1_opponent_serve_win_pct = p2_total_games_won / (p1_total_games_won + p2_total_games_won)
p2_opponent_serve_win_pct = p1_total_games_won / (p1_total_games_won + p2_total_games_won)

# Create a pie chart
labels = ['Player 1 Serve Win', 'Player 2 Serve Win', 'Player 1 Opponent Serve Win', 'Player 2 Opponent Serve Win']
sizes = [p1_serve_win_pct.mean(), p2_serve_win_pct.mean(), p1_opponent_serve_win_pct.mean(), p2_opponent_serve_win_pct.mean()]
plt.pie(sizes, labels=labels)
plt.title('Percentage of Games Won by Each Player on Serve vs. Opponent Serve')
plt.show()