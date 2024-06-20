# There is a positive correlation between the number of net points won and the number of aces hit by a player in a tennis match.

import pandas as pd
import matplotlib.pyplot as plt

# Load the data
df = pd.read_csv("Wimbledon-women-2013.csv")

# Calculate the total number of net points won by each player
df["NPW_total"] = df["NPW.1"] + df["NPW.2"]

# Create a scatter plot of NPW_total vs ACE.1
plt.scatter(df["NPW_total"], df["ACE.1"])

# Add labels and title to the plot
plt.xlabel("Net Points Won Total")
plt.ylabel("Number of Aces")
plt.title("Correlation between Net Points Won and Number of Aces")

# Show the plot
plt.show()