# The probability of the match going into a fifth set (ST5.1 and ST5.2) is positively correlated with the difference in first serve percentage between the two players (FSP.1 - FSP.2), the difference in second serve percentage between the two players (SSP.1 - SSP.2), and the difference in net points won between the two players (NPW.1 - NPW.2), while negatively correlated with the difference in unforced errors committed between the two players (UFE.1 - UFE.2) and the difference in break points won between the two players (BPW.1 - BPW.2).
import pandas as pd
import matplotlib.pyplot as plt

# read in the data from a CSV file
data = pd.read_csv('FrenchOpen-men-2013.csv')

# calculate the differences between the specified columns
data['FSP_diff'] = data['FSP.1'] - data['FSP.2']
data['SSP_diff'] = data['SSP.1'] - data['SSP.2']
data['NPW_diff'] = data['NPW.1'] - data['NPW.2']
data['UFE_diff'] = data['UFE.1'] - data['UFE.2']
data['BPW_diff'] = data['BPW.1'] - data['BPW.2']

# calculate the correlation between the differences and ST5.1/ST5.2
correlations = data[['FSP_diff', 'SSP_diff', 'NPW_diff', 'UFE_diff', 'BPW_diff', 'ST5.1', 'ST5.2']].corr()

# plot the data as a heatmap
plt.imshow(correlations, cmap='coolwarm', vmin=-1, vmax=1)
plt.xticks(range(len(correlations.columns)), correlations.columns, rotation=90)
plt.yticks(range(len(correlations.index)), correlations.index)
plt.colorbar()
plt.show()
