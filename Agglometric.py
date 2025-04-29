import numpy as np
n=int(input("Enter the number of datapoints:"))
k=int(input("Enter the size of the cluster:"))

dist=[]
'''for i in range(n):
    row=[]
    for j in range(n):
        print("i=",i,"\tj=",j)
        row.append(int(input("Enter the distance")))
    dist.append(row)
print(dist)'''
dist=[[0,1,4,5],
      [1,0,2,6],
      [4,2,0,3],
      [5,6,3,0]]     
cluster=list(range(len(dist))) 
print("c:",cluster)
while(len(cluster)>k):
    
    min_d=10
    min_i=-1
    min_j=-1
    for i in range(len(cluster)):
        for j in range(i+1,len(cluster)):
            curr_dist=dist[i][j]
            if(curr_dist<min_d):
                min_d = curr_dist
                min_i = i
                min_j = j
    new_cluster=[cluster[min_i],cluster[min_j]]
    cluster.append(new_cluster)
    print("c:",cluster)
    cluster.pop(max(min_i, min_j))
    cluster.pop(min(min_i, min_j))
    #cluster.remove(min_i)
    #cluster.remove(min_j)
    print("removed c:",cluster)

    print(f"Merged {new_cluster[0]} and {new_cluster[1]}")

print("Final clusters:")
for c in cluster:
    print(c)
