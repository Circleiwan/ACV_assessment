import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data_csv.csv')
df = df.sort_values(by=['pH', 'Gas'], na_position='first')
#df.plot.pie(x='pH', y='Gas')
df.boxplot(column=['pH', 'Gas'])
#df.plot.scatter(x='Gas', y ='Type', c='DarkBlue')
plt.show()
print(df)