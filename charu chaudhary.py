n=int(input("enter no. of elements"))
L=[]
for i in range(n):
    element=int(input("enter element"))
    L.append(element)
key=int(input("enter the element to be searched"))
for i in range (n):
    if (key==L[i]):
       print("element present at i index")
       break
else:
    print("element not found")
    