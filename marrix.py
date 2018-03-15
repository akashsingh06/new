mat=[]
for j in range(3):
    a=[]
    for i in range(3):
        element=int(input("enter the element of first mat:"))
        a.append(element)
        mat.append(a)
mat2=[]
for k in range(3):
    b=[]
    for z in range(3):
        element2=int(input("enter the elements of second mat:"))
        b.append(element2)
    mat2.append(b)

c=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(3):
    for j in range(3):
        for k in range(3):
            c[i][j]=c[i][j]+mat[i][k]*mat2[k][j]
for i in range(3):
    print(c[i])