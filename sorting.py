a=[5,7,3,8,4,9]

def swap(a):
    temp=a[k]
    a[k]=a[k+1]
    a[k+1]=temp

for j in range(0,len(a)):
 for k in range(0,len(a) -1):
     if(a[k]>a[k+1]):
         swap(a[k],a[k+1])
         
print (a)        