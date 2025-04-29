import pandas as pd
import math
df=pd.read_csv('navie_bayes_cat_training.csv')
print(df)
n=len(df)
p_cl=[]
info_d=0
list_cl=df['buys_computer'].unique()
print(list_cl)
for i in range(len(list_cl)):
    cl=0
    for j in range(n):
        if(df.loc[j][-1]==list_cl[i]):
            cl+=1
    p_cl.append(round((cl/n),3))
for j in range(len(p_cl)):
    print("p_cl",j,"=",p_cl[j],"log2=",math.log2(p_cl[j]))
    info_d+=-round((p_cl[j]*math.log2(p_cl[j])),3)
print(info_d)
for i in range(len(list_cl)):
