def fun(var):
    print(var)
    if var==5:
        return 5
    fun(var+1)
var=1
fun(var)


def  fact(num):
    if num==0 or num==1:
        return 1
    return num*fact(num-1)
num=5
print(fact(num))


def fact(sv,num):
    if sv==num:
        return 5
    return sv*fact(sv+1,num)
num=5
sv=1
print(fact(sv,num))



def add(num):
    if num==0:
        return 0
    return num%10+add(num//10)
num=2345
print(add(num))



def add(num):
    if num==0:
        return 0
    return num%10+add(num//10)
num=156
print('harshad' if num%add(num)==0 else 'not')



def carm(num,power):
    if num==0:
        return 0
    return (num%10)**power+carm(num//10,power)
num=153
print('arm' if num==carm(num,len(str(num))) else 'not')


def cdis(num,power):
    if num==0:
        return 0
    return (num%10)**power+cdis(num//10,power-1)
num=135
print('dis' if num==cdis(num,len(str(num))) else 'not')

