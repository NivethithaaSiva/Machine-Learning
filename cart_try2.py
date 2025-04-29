import pandas as pd

df=pd.read_csv("navie_bayes_cat_training.csv")

def calculate_gini(l):
    tot=len(l)
    if tot==0:
        return 0
    unique_l=l.unique()
    gini=1
    for lab in unique_l:
        p=(l==lab).sum()/tot
        gini-=p**2
    return gini

attribute=df.iloc[:,:-1]
cl=df.iloc[:,-1]
b_split=1

for att in attribute:
    unique_a=attribute[att].unique()
    for val in unique_a:
        left_s=cl[attribute[att]<=val]
        right_s=cl[attribute[att]>val]
        gini=((len(left_s)/len(cl))*calculate_gini(left_s))+((len(left_s)/len(cl))*calculate_gini(left_s))
    if(gini<b_split):
        b_split=gini
        b_att=att
        b_val=val
print(b_split,b_att,b_val)