def minthree(x,y,z):
    if x<y:
        if x<z:
            return x
    elif y<x:
        if y<z:
            return y
    else:
        return z
n1=int(input('Enter a first number:'))
n2=int(input('Enter a second number:'))
n3=int(input('Enter a third number:'))
m=minthree(n1,n2,n3)
print('Minimum of three number is:',m)