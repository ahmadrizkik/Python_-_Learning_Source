import pandas as pd

x = pd.read_csv('test3.csv', header=0, sep=',')
x.dropna(axis=0, inplace=True)
y = pd.DataFrame(x)

# print (y[0:6])

x['Duration'] = x['Duration'].astype(float)
x['Pulse'] = x['Pulse'].astype(float)
x['Maxpulse'] = x['Maxpulse'].astype(float)

# print (y.info())

print (y.describe())
