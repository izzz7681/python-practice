def factr(n):
    if n==1:
        return(n)
    else:
        return n*factr(n-1)
num=int(input('Enter a number:'))
print('The factorial of ',num,'by recursion is',factr(num))
