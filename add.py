x=[[12,7,5],
    [4,5,7],
    [6,8,9]]
y=[[13,5,7],
    [6,7,8],
    [5,7,8]]
z=[[0,0,0],
   [0,0,0],
   [0,0,0]]
for i in range(0,len(x)):
  for j in range(0,len(y)):
    for k in range(0,len(y)):
      z[i][j]+=x[i][j]*y[i][j]
      print (z[i][j])