def even(lst):
    s=0
    for n in lst:
        if n%2==0:
            s=n+1
            return s
n2=[2,3,4,6,8,9]
print(even(n2))