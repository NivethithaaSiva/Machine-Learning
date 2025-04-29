import pandas as pd
df=pd.read_csv("Adaline_training.csv")
print(df)
w=[]
dp=0
I=0
l=0
y=[]
sum_error=10
epoch=[]
n_col=len(df.columns)
for i in range(n_col):
    w.append(float(input("Enter the value of w:")))
lr=float(input("Enter the value for learning rate:"))
n=len(df)
threshold=int(input("Enter the Number of Threshold:"))
target=df.iloc[:,-1]
df.insert (0,'bias',[1,1,1,1])
print(df)
while(threshold<sum_error):
    for i in range(n):
        for j in range(n_col):
            dp+=w[j]*df.loc[i][j]
            print("x=",df.loc[i][j],"w=",w[j])
        print(dp)
        I=target[i]-dp
        y.append(I)
        print("y=",I)
       # print("j",j)
        if(I!=0):
            w[l]=round(w[l]+lr*(I)*df.loc[i][j-6],3)
            w[l+1]=round(w[l+1]+lr*(I)*df.loc[i][j-5],3)
            w[l+2]=round(w[l+2]+lr*(I)*df.loc[i][j-4],3)
            print(w)
            dp=0
            l=0
    epoch.append(w)
    sum_error=0
    for i in range(len(y)):
        sum_error+=(y[i]**2)
    print("sum_error=",sum_error)
print("threshold is less than than sum of squared error")