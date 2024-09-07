def sumpos(lst):
    s=0
    for n in lst:
        if n>=0:
            s=s+n
        return s
lst1=[3,-3,5,20,-1]
print('Sum of positive no. is:',sumpos(lst1))