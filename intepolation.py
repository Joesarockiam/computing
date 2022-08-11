def interpolation(d, x):
   output = d[0][1] + (x - d[0][0]) * ((d[1][1] - d[0][1])/(d[1][0] - d[0][0]))
   return output
data=[[300,2.4771],[304,2.4829]]
x=301
print("x=301=>f(x)=".format(x),interpolation(data,x))
