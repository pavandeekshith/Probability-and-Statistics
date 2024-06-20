# The first serve percentage (FSP.1) and first serve won (FSW.1) of Player 1 have a positive correlation with the probability of them winning the match in straight sets (ST1.1, ST2.1, ST3.1). Conversely, the number of unforced errors committed by Player 2 (UFE.2) and the number of break points won by Player 2 (BPW.2) have a negative correlation with the probability of Player 1 winning the match in straight sets.
import pandas as pd

df = pd.read_csv('FrenchOpen-men-2013.csv')
# create a new column for the total number of sets won by Player 1
df['sets_won_by_p1'] = df['ST1.1'] + df['ST2.1'] + df['ST3.1']

# calculate the correlation between the variables
corr = df[['FSP.1', 'FSW.1', 'UFE.2', 'BPW.2', 'sets_won_by_p1']].corr()

# print the correlation matrix
# print(corr)

import matplotlib.pyplot as plt

plt.scatter(df['FSP.1'], df['ST1.1'])
plt.xlabel('First Serve Percentage for Player 1')
plt.ylabel('Set 1 Result for Player 1')
plt.title('Correlation between First Serve Percentage and Set 1 Result')
plt.show()