import numpy as np
import pandas as pd
df=pd.read_csv('multi.csv')
l=len(df.columns)
n=[]
x=[]
xt=[]
xtx=[]
xtr=[]
w=[]
r=[]
for i in range(l):
    w.append(0)
for i in range(len(df)):
    n.append(list(df.loc[i]))
x=[[1]+row[:-1]for row in n]
r=[row[-1]for row in n]
xt=np.transpose(x)
xtx=np.dot(xt,x)
xtr=np.dot(xt,r)
t=0
for i in range(l):
   t=np.dot(xtx[i],w)
   temp=xtx[i][i]*w[i]
   res=(xtr[i]-(t-temp))/xtx[i][i]
   w[i]=res
print(w)