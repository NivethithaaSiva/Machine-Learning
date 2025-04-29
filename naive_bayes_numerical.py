def max_cl(value,cl):
    max_num=value[0]
    max_cl=cl[0]
    for i in range(len(value)):
        if value[i] > max_num :
            max_cl =cl[i] 
    return max_cl
import pandas as pd
import math
df=pd.read_csv("navie_bayes_num_training.csv")
q=[]
print(df)
print("Enter the values of query:")
for i in range(2):
    a1=int(input())
    q.append(a1)
temp=0
count=0
m=0
s=0
p=[]
mue=[]
matrix=[]
n_col=len(df.columns)
temp1=0
p_cl=[]
sigma=[]
prob=1
ans=[]
n=len(df)
list_cat=df['cl'].unique()
for i in range(len(list_cat)):
    print("FOR CLASS LABEL",list_cat[i])
    for j in range(n):
        if(df.loc[j][-1]==list_cat[i]):
            matrix.append(list(df.loc[j]))
            temp+=1
    temp1=temp/n
    p_cl.append(temp1)
    print("p(",list_cat[i],")=",temp1) 
    for k in range(n_col-1):
        for r in range(len(matrix)):
            count+=matrix[r][k]
        m=count/temp
        mue.append(round(m,3))
        m=0        
        count=0
    print("mue=",mue)
    for k in range(n_col-1):
        for r in range(len(matrix)):
            s+=(matrix[r][k]-round(mue[k],3))**2
        sig=round((math.sqrt(round(s,3)/temp)),3)
        print("sigma=",sig)
        sigma.append(sig)
        s=0
    for k in range(len(q)):
        v=round((2*(sigma[k]**2)),3)
        c=round(math.exp((-1)*(((q[k]-mue[k])**2)/v)),3)
        temp2=1/(2.506*sigma[k])
        temp3=round(c,3)*temp2
        print("p(x/c",k+1,")=",round(temp3,3))
        p.append(round(temp3,3))
    print(p)
    for v in range(len(p)):
        prob*=round(p[v],3)
    prob1=round(prob*p_cl[i],5)
    ans.append(prob)
    print("p(x=",q,"/c=",list_cat[i],")=",prob1)
    temp1=0
    temp=0
    count=0
    matrix=[]
    mue=[]
    sigma=[]
    p=[]
    prob=1
    print("`````````````````````````````````````````````````````")      
probability=max_cl(ans,list_cat)
print("THE GIVEN QUERY",q,"BELONG TO:",probability)