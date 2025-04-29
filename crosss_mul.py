import pandas as pd
import math
one=pd.read_csv('cross_ent_mul.csv')
y=pd.read_csv('cross_data.csv')
print(one)
sum1=0
summ=[]
cels=[]
cel=0
f=[]
for i in range(len(y)):
    for j in range(len(y)):
        sum1+=math.exp(y.loc[i][j])
    summ.append(sum1)
    sum1=0
for i in range(len(y)):
    for j in range(len(y)):
        sum3=math.exp(y.loc[i][j])/summ[i]
        f.append(sum3)
    for k in range(len(one)):
        cel+=-(-one.loc[i][k]*math.log2(f[i]/summ[i]))
    cels.append(cel)
    cel=0
print(cels)