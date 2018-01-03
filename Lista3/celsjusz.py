from random import randint

def celtofar(n):
    x=32+((9/5)*n)
    return x

def fartocel(n):
    x=(5/9)*(n-32)
    return x
#fahrenheit na celsjusz

def gentemp(n):
    x=[]
    for a in range(n):
        z=randint(-50, 50)
        x.append(z)
    return x


