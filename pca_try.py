import pandas as pd
df=pd.read_csv('pca_data.csv')

x=list(df['x'])
y=list(df['y'])
n=len(df)
l=len(df.columns)
x_mean=sum(x)/n
y_mean=sum(y)/n

xi=[]
yi=[]
xiyi=[]
cov_x=0
cov_y=0
cov_xy=0
cov=[]
temp=[]
for i in range(n):
    xi.append(round((x[i]-x_mean),3))
    yi.append(round((y[i]-y_mean),3))
    xiyi.append(round((xi[i]*yi[i]),3))
for i in range(n):
    cov_x+=(xi[i]**2)/(n-1)
    cov_y+=(yi[i]**2)/(n-1)
    cov_xy+=(xiyi[i])/(n-1)
for i in range(l):
    for j in range(l):
        if(i==j):
            if(j==0):
                temp.append(cov_x)
            else:
                temp.append(cov_y)
        else:
            temp.append(cov_xy)
    cov.append(temp)
    temp=[]
print(cov)