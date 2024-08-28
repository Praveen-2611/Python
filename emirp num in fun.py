def is_pali(num,copy,rev=0):
    while num != 0:
        ld=num%10
        rev=rev*10+ld
        res=rev
        num//=10
    return copy != rev
def is_prime(num):
    for fa in range(2,num//2+1):
        if(num%fa==0):
            return False
        return True
    for fa in range(2,res//2+1):
        if(res%fa==0):
            return False
        return True
num=18
print('emirp' if is_pali(num,num) and is_prime(num) else 'not')
