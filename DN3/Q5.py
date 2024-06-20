import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv("USOpen-men-2013.csv")
print(data.head(0))
data['TPW_diff'] = data['TPW.1'] - data['TPW.2']
corr = data[['TPW_diff', 'BPC.1', 'NPA.1', 'FNL1', 'DBF.2']].corr()
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title("Correlation Matrix")
plt.show()