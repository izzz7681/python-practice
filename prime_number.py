n=int(input('enter number to find if it is prime or not:'))
prime=1
i=2
while i<=n-1:
    if n%i==0:
        prime=0
    i=i+1
if prime ==1:
    print(n,'is prime!')
else:
    print(n,'is not prime!')