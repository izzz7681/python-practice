def maxtwo(x,y):
    if x>y:
        return x
    else:
        return y
n1=int(input('Enter first number:'))
n2=int(input('Enter second number:'))
m=maxtwo(n1,n2)
print('Maximum of two is',m)