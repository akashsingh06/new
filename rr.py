riya=open("riya.txt","r+")
print("name is ",riya.name)
print("mode is ",riya.mode)
str=riya.read()
riya.close()
print(str)