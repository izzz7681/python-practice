a=int(input('Enter first number:'))
b=int(input('Enter second number:'))
c=int(input('Enter third number:'))
if (a<b)&(a<c):
    print(a,'is smallest')
elif(b>c)&(b>a):
    print(b,'is smallest')
else:
    print(c,'is smallest')