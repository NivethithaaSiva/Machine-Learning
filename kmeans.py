
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 16:15:48 2023

@author: 21X03
"""

import pandas as pd
import math
import statistics 
file=pd.read_csv("k_means_data.csv")
k=int(input("Enter the k value(1 to {}):".format(len(file))))
ran=[]
print("Enter",k,"Random points:")
for i in range(k):
    ran.append(int(input()))
flag=True
while(flag):
    dis=[]
    for i in range(k):
        d=[]
        for j in range(len(file)):
            temp=0
            for k in range(len(file.columns)):
                temp+=round((file.loc[ran[i]-1][k]-file.loc[j][k])**2,3)
            temp=math.sqrt(round(temp,3))
            d.append(round(temp,3))
        dis.append(d)
    print("DISTANCE:",dis)
    minimum=[]
    minindex=[]
    mindp=[]
    for i in range(len(dis[0])):
        val=[]
        for j in range(len(dis)):
            val.append(dis[j][i])
        minimum.append(min(val))
        minindex.append(ran[val.index(min(val))])
    print(minimum,"\n",minindex)
    cat=list(set(minindex))
    cat.sort()
    #print(cat)
    cluster=[]
    for i in range(len(cat)):
        temp=[]
        for j in range(len(minindex)):
            if cat[i]==minindex[j]:
                temp.append(j)
        cluster.append(temp)
    print("cluster:",cluster)
    a1=[]
    res_a=[]
    result=[]
    for i in range(len(cluster)):
        for j in range(len(file.columns)):
            for k in range(len(cluster[i])):
                a1.append(file.loc[cluster[i][k]][j])
            m=sum(a1)/float(len(a1))
            res_a.append(m)
        result.append(res_a)
        res_a=[]
    for i in range(len(ran)):
        print("Mean(Cluster",i+1,")(DP",ran[i],"):",result[i])
    flag=False