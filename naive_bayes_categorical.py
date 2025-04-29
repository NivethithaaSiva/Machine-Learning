def classlabe_max(classlabel,value):
    temp=classlabel[0]
    for i in range(1,len(value)):
        if(value[i]>value[i]):
            temp=class_label[i]
    return temp
import pandas as pd
df=pd.read_csv("navie_bayes_cat_training.csv")
#print(df)
q=[]
cx=0
matrix=[]
col=len(df.columns)-1
#index=list(df.keys())
#print("headers of the file:",index)
n=len(df)
p=[]
p_query=[]
p_result=[]
q_age=input("Enter the age(youth/middle aged/senior):")
q.append(q_age)
q_income=input("Enter the income(high/medium/low):")
q.append(q_income)
q_student=input("Enter the student(yes/no)")
q.append(q_student)
q_credit=input("Enter the credit(fair/excellent):")
q.append(q_credit)

list_cat=df['buys_computer'].unique()

len_comp=len(list_cat)

count=0
l=0
m=0
temp=0
for i in range(len_comp):
    for j in range(n):
      if(df.loc[j][-1]==list_cat[l]):
            matrix.append(list(df.loc[j]))
            count=count+1
    #print(matrix)
    for k in range(col):
        for r in range (len(matrix)):
            if(matrix[r][k]==q[k]):
               temp=temp+1
            temp1=temp/count
        print("",q[k]," temp=",temp,"temp1=",round(temp1,3))
        p_query.append(round(temp1,3))
        print("p_query=",p_query)
        temp=0
    temp2=1
    for a in range(len(p_query)):
        temp2*=p_query[a]
         
    print("```````````````````````````````````````````````````````````````````````")
    print("count for,",list_cat[l],":",count)
    cx=count/n
    print("p(x=",q,"/c1=",list_cat[l],")=",round(temp2,3))  
    print("p(c1=",list_cat[l],")=",round(cx,3))
    ans=cx*temp2
    print("p(c1=",list_cat[l],"/query=",q,")=",round(ans,3))
    print("```````````````````````````````````````````````````````````````````````")
    p.append(round(cx,3))
    count=0
    l+=1
    p_result.append(round(ans,3))
    matrix=[]
    p_query=[]
class_label=classlabe_max(list_cat,p_result)  
print(class_label)
