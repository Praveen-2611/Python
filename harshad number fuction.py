def is_harshad(var,copy,res=0):
    while var != 0:
        ld=var%10
        res+=ld
        var//=10
    if copy%res==0:
        return True
    return False
var=155
print('harshad' if is_harshad(var,var) else 'not')
