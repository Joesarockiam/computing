import math as m
def func( x ):
    return 2*x*x+5-m.exp(x)
def derivFunc( x ):
    return 4*x-m.exp(x)
def newtonRaphson( x ):
    h = func(x) / derivFunc(x)
    while abs(h) >= 0.0001:
        h = func(x)/derivFunc(x)
        x = x - h
    print("The value of the root is : ","%.4f"% x)
x0 =3.5
newtonRaphson(x0)
