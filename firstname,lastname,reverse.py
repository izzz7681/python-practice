def printname(firstname, lastname, reverse=False):
    if reverse:
        print(lastname + ' ' + firstname)
    else:
        print(firstname + ' ' + lastname)

printname('Izma', 'Shaikh')
printname('Izma', 'Shaikh', False)
printname('Izma', 'Shaikh', True)
