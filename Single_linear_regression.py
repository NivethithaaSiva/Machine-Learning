import matplotlib.pyplot as plt
import pandas as pd
df=pd.read_csv('single_lin_reg.csv')
print(list(df.loc[0]))
x=df.loc[0]
r=df.loc[1]
xr=0
x_mean=0
r_mean=0
n=0
k=0
g=[]
time=[]
x_summation_sq=0
for i in range(len(x)):
    n+=1
    xr+=x[i]*r[i]
    x_mean+=x[i]/len(x)
    r_mean+=r[i]/len(x)
    x_summation_sq+=pow(x[i], 2)
w1=(xr-(r_mean*x_mean*n))/(x_summation_sq-(pow(x_mean,2)*n))
print("w1=",w1)
wo=r_mean-(x_mean*w1)
print("w2=",wo)
for i in range(0,n):
    time.append(df.loc[0][i])
    k=wo+(w1*x[i])
    g.append(k)
    print("g(",i+1,")=",k)
print(g,"\n",time)
print(wo,"\t",w1)
v=int(input("ENTER THE VALUE OF X:"))
k=wo+(w1*v)
print("g:",k)
g.append(round(k,2))
#r.append(k)
time.append(v)
#print(x," ",g)
#print("g(",v,")=",k)
print(time,"\n",g)
plt.plot(time,g)
plt.show()

