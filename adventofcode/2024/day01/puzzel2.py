import pandas as pd

df = pd.read_csv('day1-1.csv', header=None, sep=r'\s{3}')
df.columns = ['c1','c2']

col1 = df['c1'].tolist()
col2 = df['c2'].tolist()

sum = 0

for i in col1:
    for j in col2:
        if i == j:
            sum += i

print (sum)