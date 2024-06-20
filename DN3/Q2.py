# If a player has a higher percentage of net points, they may also have a higher percentage of unforced errors.
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("AusOpen-women-2013.csv")

# Calculate the percentage of net points won by each player
p1_net_points_pct = df['NPW.1'] / df['NPA.1']
p2_net_points_pct = df['NPW.2'] / df['NPA.2']

# Calculate the percentage of unforced errors made by each player
p1_unforced_errors_pct = df['UFE.1'] / (df['UFE.1'] + df['WNR.1'] + df['WNR.1'] + df['ACE.1'])
p2_unforced_errors_pct = df['UFE.2'] / (df['UFE.2'] + df['WNR.2'] + df['WNR.2'] + df['ACE.2'])

# Plot the data
plt.scatter(p1_net_points_pct, p1_unforced_errors_pct, color='red', label='Player 1')
plt.scatter(p2_net_points_pct, p2_unforced_errors_pct, color='blue', label='Player 2')
plt.xlabel('Percentage of Net Points Won')
plt.ylabel('Percentage of Unforced Errors')
plt.title('Correlation between Net Points Won and Unforced Errors')
plt.legend()
plt.show()