def is_sunny(var,num=0):
    while num*num <= var+1:
        if num*num==var+1:
            return True
        num+=1
    return False
var = 24
print('sunny number' if is_sunny(var) else 'not sunny number')

