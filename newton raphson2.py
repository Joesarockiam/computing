def func( x ):
    return x*x*x*x -5*x*x*x+9*x+3
def derivFunc( x ):
    return 4*x*x*x-15*x*x+9
def newtonRaphson( x ):
    h = func(x) / derivFunc(x)
    while abs(h) >= 0.0001:
        h = func(x)/derivFunc(x)
        x = x - h
    print("The value of the root is : ","%.4f"% x)
x0 =5
newtonRaphson(x0)
