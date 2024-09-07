num=int(input('Enter a number:'))
r=int(input('Enter range for multiplication table:'))
for i in range(1,r+1):
    print(num,'*',i,'=',(num*i))
