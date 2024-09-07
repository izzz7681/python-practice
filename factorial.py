n=int(input('Enter number to find its factorial:'))
fac =1
while fac<=n:
    if n%fac==0:
        print(fac,'is factor of',n)
    fac=fac+1