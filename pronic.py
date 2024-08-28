def is_pronic(var,num=0):
    while num*num+1 <= var:
        if num*num+1==var:
            return True
        num+=1
    return False
var = 14
print('Pronic number' if is_pronic(var) else 'not pronic number')
