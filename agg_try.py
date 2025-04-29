dist=[[0,1,4,5],
      [1,0,2,6],
      [4,2,0,3],
      [5,6,3,0]]
c=list(range(len(dist)))
n=4
k=2

while(len(c)>k):
    min_d=10
    min_i=-1
    min_j=-1
    for i in range(len(c)):
        for j in range(i+1,len(c)):
            curr_dist=dist[i][j]
            if(curr_dist<min_d):
                min_d=curr_dist
                min_i=i
                min_j=j
    new_cluster=[c[min_i],c[min_j]]
    c.append(new_cluster)
    print(c)
    c.pop(max(min_i,min_j))
    print(c)
    c.pop(min(min_i,min_j))
    print(c)
    print(f"Merged {new_cluster[0]} and {new_cluster[1]}")
for i in c:
    print(i)