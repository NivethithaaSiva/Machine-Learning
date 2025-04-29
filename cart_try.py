import pandas as pd
df=pd.read_csv("navie_bayes_cat_training.csv")

def calculate_gini(l):
    tot=len(l)
    if tot==0:
        return 0
    unique_l=l.unique()
    gini=1
    
    for lab in unique_l:
        p=(lab==l).sum()/tot
        print((lab==l).sum())
        gini-=p**2
    return(round(gini,4))

attribute=df.iloc[:,:-1]
b_gini=1
cl=df.iloc[:,-1]

for att in attribute:
    print("att=",att)
    unique_a=attribute[att].unique()
    print("unique_A:",unique_a)
    
    for val in unique_a:
        #print("cl[attribute[att]<=val]",cl[attribute[att]<=val])
        left_s=cl[attribute[att]<=val]
        right_s=cl[attribute[att]>val]
       # print("left:",left_s,"right:",right_s)
        
        gini=(len(left_s)/len(cl))*calculate_gini(left_s)+(len(right_s)/len(cl))*calculate_gini(right_s)
        print("gini:",gini)
        
        if(gini<b_gini):
            b_gini=gini
            b_att=att
            b_s_v=val
print("Best Attribute:", b_att)
print("Best Split Value:", b_s_v)
print("Best Gini:", b_gini)