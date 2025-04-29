import numpy as np
import pandas as pd
import math
df=pd.read_csv('poly.csv')
n=len(df)
r=[]
w=[]
rx_sum=0
summation=0
t=0
matrix=[]
poly_matrix=[]
k=int(input("enter the k order:"))
for i in range(k+1):
    w.append(0)
    for j in range(k+1):
        t=i+j
        if(t==0):
            matrix.append(n)
        else:
            for v in df['x']:
                summation+=math.pow(v,t)
            matrix.append(summation)
            summation=0
    for v1,v2 in zip(df['r'],df['x']):
        rx_sum+=v1*math.pow(v2, i)
    r.append(rx_sum)
    rx_sum=0
    poly_matrix.append(matrix)
    matrix=[] 
print(poly_matrix)
print(r)
for i in range(k+1):
    t=np.dot(poly_matrix[i],w)
    temp=poly_matrix[i][i]*w[i]
    res=(r[i]-(t-temp))/poly_matrix[i][i]
    w[i]=res
print(w)