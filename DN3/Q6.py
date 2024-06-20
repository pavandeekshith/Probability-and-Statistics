import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("USOpen-women-2013.csv")

# Calculate the correlation between first serve points won and second serve points won
corr = df['FSW.1'].corr(df['SSW.1'])

# Print the correlation coefficient
print("Correlation between first serve points won and second serve points won:", corr)

# Create a scatter plot of the data
plt.scatter(df['FSW.1'], df['SSW.1'])
plt.xlabel('First serve points won')
plt.ylabel('Second serve points won')
plt.title('Correlation between first serve points won and second serve points won')
plt.show()