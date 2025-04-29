import pandas as pd
import math
df=pd.read_csv("expectation_max.csv")
print(df)
column=[]
for i in df:
    print(i)
    column.append(i)
#p=float(input("Enter the prob of seq1:"))
#q=float(input("Enter the prob of seq2:"))
h_a=[]
h_b=[]
t_a=[]
t_b=[]
p=0.6
q=0.5
p_a=0.5
p_b=0.5
h=0
t=0
l=0
cl=df['seq1'].unique()
print(cl)
#column=['seq1','seq2']
for i in column:
    seq1=df[i]
    for j in range(len(seq1)):
        if(seq1[j]=='h'):
            h+=1
        if(seq1[j]=='t'):
            t+=1
    print(h,t)
    p_s_a=round(math.pow(p,h)*math.pow((1-p),t),5)
    p_s_b=round(math.pow(q,h)*math.pow((1-q),t),5)
    p_s=round((p_s_a*p_a)+(p_s_b*p_b),5)
    p_a_s=round((p_s_a*p_a)/p_s,4)
    p_b_s=round((p_s_b*p_b)/p_s,4)
    
    e_a_h=round(h*p_a_s,3)
    h_a.append(e_a_h)
    e_a_t=round(t*p_a_s,3)
    t_a.append(e_a_t)
    
    e_b_h=round(h*p_b_s,3)
    h_b.append(e_b_h)
    e_b_t=round(t*p_b_s,3)
    t_b.append(e_b_t)
    print("Expectated heads and tails for a=",e_a_h,e_a_t)
    print("Expectated heads and tails for b=",e_b_h,e_b_t)
    h=0
    t=0
sum_h=0
total=0
for i in range(len(h_a)):
    total+=h_a[i]+t_a[i]
    sum_h+=h_a[i]
p=round(sum_h/total,3)

sum_h=0
total=0
for i in range(len(h_b)):
    total+=h_b[i]+t_b[i]
    sum_h+=h_b[i]
q=round(sum_h/total,3)

print("updated values p=",p,"\tq=",q)