import numpy as np
import pandas as pd
import math
df=pd.read_csv('log.csv')
n=len(df)
n_col=len(df.columns)
y=[]
w=[]
t=0
y_pred=[]
pred=0
for i in range(n_col):
    w.append(0)
for i in range(n):
    print("dp",i,":")
    x=[]
    for j in range(n_col):
        if(j==0):
            t+=w[j]
            x.append(1)
        else:
            t+=w[j]+df.loc[i][j-1]
            x.append(df.loc[i][j-1])
    pred=1/(1+math.exp(-1*t))
    t=0
    if(pred>0.5):
        y_pred.append(1)
    else:
        y_pred.append(0)
    for k in range(n_col):
        w[k]=w[k]+0.3*(df.loc[i][n_col-1]-pred)*pred*(1-pred)*x[k]
        print(w[k])