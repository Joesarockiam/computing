def interpolation(d, x):
   output = d[0][1] + (x - d[0][0]) * ((d[1][1] - d[0][1])/(d[1][0] - d[0][0]))
   return output
data=[[9,14],[11,16]]
x=10
print("x=10=>y=".format(x),interpolation(data,x))
