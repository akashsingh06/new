
def 
    for i in range(len(l)):
        for j in range(len(l)-1-i):
            if l[j]>l[j+1]:
                temp=l[j]
                l[j]=l[j+1]
                l[j+1]=temp
                return 1
l=[]
n=int(input('enter the number of elements u want in the list'))
for i in range(n):
    p=int(input("enter the element"))
    l.append(p)
t=trouble_sort(1)
print(t)