import pandas as pd
df=pd.read_csv('pca_data.csv')
n=len(df)
l=len(df.columns)
x=list(df['x'])
y=list(df['y'])
xmean=sum(x)/n
ymean=sum(y)/n
xi=[]
yi=[]
xiyi=[]
cvm=[]
cxx=0
cyy=0
cxy=0
temp=[]
for i in range(n):
    xi.append(round(x[i]-xmean,1))
    yi.append(round(y[i]-ymean,1))
    xiyi.append(round(xi[i]*yi[i],2))
for i in range(n):
    cxx+=round((xi[i]**2)/(n-1),2)
    cyy+=round((yi[i]**2)/(n-1),2)
cxy=round(sum(xiyi)/(n-1),1)
cxx=round(cxx,1)
cyy=round(cyy,1)
for i in range(l):
    for j in range(l):
        if(i==j):
            if(j==0):
                temp.append(cxx)
            else:
                temp.append(cyy)
        else:
            temp.append(cxy)
    cvm.append(temp)
    temp=[]
print(cvm)
