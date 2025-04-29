import pandas as pd
import numpy as np
df=pd.read_csv("Rosenblatt's_perceptron_training.csv")
print(df)
w=[]
dp=0
y=[]
l=0
epoch=[]
n_col=len(df.columns)
for i in range(n_col-1):
    w.append(float(input("Enter the value of w:")))
threshold=int(input("Enter the threshold value:"))
lr=float(input("Enter the learning rate value:"))
n=len(df)
epo=int(input("Enter the Number of epoch:"))
target=df.iloc[:,-1]
for k in range(epo):
    for i in range(n):
        for j in range(n_col-1):
            dp+=w[j]*df.loc[i][j]
            print("x=",df.loc[i][j],"w=",w[j])
        print(dp)
        if(dp>=1):
            y.append(int(1))
        else:
            y.append(int(0))
        if(y[i]!=target[i]):
            w[l]=round(w[l]+lr*(target[i]-y[i])*df.loc[i][j-1],3)
            w[l+1]=round(w[l+1]+lr*(target[i]-y[i])*df.loc[i][j],2)
            print(w)
            dp=0
            l=0
    epoch.append(w)
for i in range(len(epoch)):
    for j in range(len(epoch[i])):
        if(epoch[i]==epoch[j]):
            v=True
        else:
            v=False
if(v==True):
    print("Epoch's are equal")
else:
    print("Epoch's are not equal")