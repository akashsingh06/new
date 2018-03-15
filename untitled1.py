L1=[[1,2,3],[4,5,6],[7,8,9]]
L2=[[9,8,7],[6,5,4],[3,2,1]]
L3=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(0,len(L1)):
    for j in range(0,len(L2[i])):
        for k in range(len(L2)): 
         L3[i][j]=L1[i][k]*L2[k][j]+L3[i][j]            
print (L3)
for r in L3:
    print(r)