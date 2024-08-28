def carm(num,dup,ndig,sol=0):
    while num!=0:
        ld=num%10
        sol=sol+ld**ndig
        num//=10
    return dup==sol
num = 153
if carm(num,num,len(str(num))):
    print('arm')
else:
    print('not')


def cdis(num,dup,ndig,sol=0):
    while num!=0:
        ld=num%10
        sol=sol+ld**ndig
        num//=10
        ndig-=1
    return dup==sol
num = 135
if cdis(num,num,len(str(num))):
    print('dis')
else:
    print('not')


def isprime(num):
    for fa in range(2,num//2+1):
        if num%fa==0:
            return 'not prime'
        return 'prime'
num=17
print(isprime(num))


def fact(num):
    res=1
    for val in range(1,num+1):
        res=res*val
    return res
num=3
print(fact(num))


def fact(num,mul=1):
    for val in range(1,num+1):
        mul=mul*val
    return mul
def is_digit(num,copy,dsum=0):
    while num!=0:
        ld=num%10
        dsum+=fact(ld)
        num//=10
    return copy==dsum
def special(num):
    return  is_digit(num,num)
num=145
print('sp' if special(num) else 'not')



def square(num,dsum=0):
    while num!=0:
        ld=num%10
        dsum=dsum=ld**2
        num//=10
        return dsum
def check(num):
    while num>9:
        num=square(num)
    return num==1 or num==7
num=19
print('h' if check(num) else 'n')
            

    
        
