import pandas as pd
df = pd.read_csv('Madaline_training.csv')
print(df)
w = []
y = 1
z = []
b = []
v = []
zin=[]
target = df.iloc[:, -1]
print(target != y)
n_col = len(df.columns) - 1
for i in range(n_col):
    row = []
    for j in range(n_col):
        row.append(float(input("Enter the value of weight(i/p-hidden): ")))
    w.append(row)
print("w=",w)
for i in range(n_col):
    b.append(float(input("Enter the value of bias: ")))
print("b=",b)
bo = float(input("Enter the value of o/p bias: "))
for i in range(n_col):
    v.append(float(input("Enter the value of weight(hidden-o/p): ")))
print("v=",v)
lr=float(input("Enter the learning rate value:"))
yin=bo
zi = 0
for m in range(len(df)):
    for n in range(2):
        for j in range(n_col):
            zi=b[j]
            for i in range(n_col):
                zi += w[i][j]*df.loc[m][i]
            zin.append(zi)
            zi=0
        for k in range(len(zin)):
            if(zin[k]>=0):
                z.append(1)
            else:
                z.append(0)
        for l in range(len(v)):
            yin+=round(z[l]*v[l],3)
        print("yin=",yin)
        if(yin>=0):
            y=1
        else:
            y=0
        if(target[m]!=y):
            for j in range(n_col):
                for i in range(n_col):
                    w[j][i]= w[i][j]+(lr*(target[m]-zin[i]))*df.loc[m][i]
            for k in range(len(b)):
                b[k]=b[k]+(lr*(target[m]-zin[k]))
        print("updated weights:",w)
        print("updated bias:",b)
        print("``````````````````````````````````````````````````````````")
        y=0