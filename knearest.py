import pandas as pd
import math
t1=pd.read_csv('k_training.csv')
t2=pd.read_csv('k_test.csv')
n=len(t1.columns)
cl=[]
temp=0
dist=[]
k=3
for i in range(len(t2)):
    for j in range(len(t1)):
        cl.append(t1.loc[j][n-1])
        dp=t1.loc[j]
        q=t2.loc[i]
        dp=dp[:-1]
        for k in range(len(dp)):
            temp+=((q[k]-dp[k])**2)
        temp1=math.sqrt(temp)
        dist.append(temp1)
        temp=0
        print(len(dist))
    for l in range(len(dist)):
        for a in range(l+1,len(dist)):
               if(dist[l]>dist[k]):
                   temp2=dist[l]
                   dist[l]=dist[a]
                   dist[a]=temp2
                   temp3=cl[l]
                   cl[l]=cl[a]
                   cl[a]=temp3
        dist=[]
        temp4=cl[:(k-len(cl))]
        q_label=max(temp4,key=cl.count)
        print("CLASS LABEL OF",q_label)
        cl=[]