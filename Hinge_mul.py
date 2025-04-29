f=open("hinge_multiple.data",mode="r")
category=[]
f1=[]
f2=[]
f3=[]
syi=0
yi=[]
for each in f:
    split_list=each.split(',')
    category.append(split_list[0])
    f1.append(split_list[1])
    f2.append(split_list[2])
    f3.append(split_list[3])
category.remove('')
#print(category)
for i in range(len(category)):
    if(category[i]==f1[0]):
        syi=float(f1[i+1])
        yi.append(float(f2[i+1]))
        yi.append(float(f3[i+1]))
    elif(category[i]==f2[0]):
        syi=float(f2[i+1])
        yi.append(float(f1[i+1]))
        yi.append(float(f3[i+1]))
    elif(category[i]==f3[0]):
        syi=float(f3[i+1])
        yi.append(float(f1[i+1]))
        yi.append(float(f2[i+1]))
    for j in yi: 
        svm=max(0,(syi-j+1))
        print(svm)
    svm=0
    y=[]
