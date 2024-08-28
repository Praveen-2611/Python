'''
n=5
for line in range(n+1):
    print('*'*line)

print('-'*30)


n = 5
for line in range(n,0,-1):
    print('*'*line)


print('-'*30)

n=5
spaces=0
stars=5
for line in range(n,0,-1):
    for space in range(spaces):
        print(' ',end=' ')
        
    for star in range(stars):
        print('*',end=' ')
    spaces+=1
    stars-=1
    print()

print('-'*30)

n=4
spaces=n-1
stars=1
for line in range(1,n+1):
    for space in range(spaces):
        print(' ',end=' ')
    for star in range(stars):
        print('*',end=' ')
    spaces-=1
    stars+=2
    print()

print('-'*30)

n=5
spaces=0
stars=(n*2)-1
for line in range(1,n+1):
    for space in range(spaces):
        print(' ',end=' ')
    for star in range(stars):
        print('*',end=' ')
    spaces+=1
    stars-=2
    print()

print('-'*30)

n=4
num=1
spaces=n-1
stars=1
for line in range(1,n+1):
    for space in range(spaces):
        print(' ',end=' ')
    for star in range(stars):
        print(str(num),end=' ')
    stars+=2
    spaces-=1
    num+=1
    print()

print('-'*30)


n=5
for line in range(n+1):
    for col in range(line):
        print(line,end=' ')
    print()
print('-'*30)

n=6
for line in range(n,1,-1):
    for col in range(line):
        print(line,end=' ')
    print()

print('-'*30)

n=5
var=n
for line in range(n+1):
    for col in range(line):
        print(var,end=' ')
    var-=1
    print()
    
print('-'*30)

n=5
spaces=n-1
for ev in range(4,-1,-1):
    for space in range(spaces):
        print(' ',end=' ')
    for sv in range(5,ev,-1):
        print(sv,end=' ')
    print()
    spaces-=1

print('-'*30)

#procedural programs

n=4
if n%2==0:
    print('even')
else:
    print('odd')
print('-'*30)


n=5
fact=1
for val in range(1,n+1):
    fact*=val
print(fact)
print('-'*30)


n=1551
dup=n
rem=0
while n != 0:
    ld=n%10
    rem=rem*10+ld
    n//=10
if rem==dup:
    print('palindrome')
else:
    print('not')

print('-'*30)

n=153
dup=n
rem=0
while n != 0:
    ld=n%10
    rem=rem+ld**3
    n//=10
if dup==rem:
    print('armstrong')
else:
    print('not')
print('-'*30)

n=135
dup=n
rem=0
count=len(str(n))
while n != 0:
    ld=n%10
    rem=rem+ld**count
    n//=10
    count-=1
if dup==rem:
    print('disarm')
else:
    print('not')
print('-'*30)

n=145
dup=n
rem=0
while n != 0:
    ld=n%10
    fact=1
    for val in range(1,ld+1):
        fact*=val
    rem+=fact
    n//=10
if dup==rem:
    print('special')
else:
    print('not')

print('-'*30)

n=77
dup=n
rem=0
while n != 0:
    ld=n%10
    rem=rem*10+ld
    n//=10
if dup==rem:
    for val in range(2,n//2+1):
        print('not palyprime')
        break
    else:
        print('palyprime')
else:
    print('not palyprime')

print('-'*30)

n=171
dup=n
rem=0
while n!=0:
    ld=n%10
    rem+=ld
    n//=10
print('harshad' if dup%rem==0 else'not')

print('-'*30)


n,dup,rem=41,n,0
while n!=0:
    rem=(rem*10)+n%10
    n//=10
if dup!=rem:
    count=0
    for val in range(2,dup//2+1):
        if dup%val==0:
            count+=1
    if count==0:
        count1=0
        for val1 in range(2,rem//2+1):
            if rem%val1==0:
                count1+=1
        if count1==0:
            print('emirp')
        else:
            print('not emirp')
    else:
        print('not emirp')
else:
    print('not emirp')
print('-'*30)

n=15
ans=0
position=1
while n!=0:
    ld=n%2
    ans+=ld*position
    position*=10
    n//=2
print(ans)
print('-'*30)


n=1111
ans=0
power=0
while n!=0:
    rem=n%10
    ans+=rem*2**power
    power+=1
    n//=10
print(ans)
print('-'*30)

n=68
while n>9:
    dsum=0
    while n !=0:
        ld=n%10
        dsum+=ld**2
        n//=10
    n=dsum
if n==1 or n==7:
    print('happy')
else:
    print('not')
print('-'*30)

n=192
check=(str(n)+str(n*2)+str(n*3))
for val in range (1,10):
    if str(val)not in check:
        print('not facinating')
        break
else:
    print('facinating')

print('-'*30)

var=90
n=0
while n*(n+1)<=var:
    if n*(n+1)==var:
        print('pronic')
        break
    n+=1
else:
    print('not')
      
print('-'*30)

var=24
n=0
while n*n<=var+1:
    if n*n==var+1:
        print('sunny number')
        break
    n+=1
else:
    print('not')
print('-'*30)

#functional programs

def is_prime(num):
    for val in range(2,num//2+1):
        if num%val==0:
            return 'notprime'
        return 'prime'
num=17
print(is_prime(num))
print('-'*30)

def is_armstrong(num,dup,rem=0):
    while num != 0:
        ld=num%10
        rem=rem+ld**3
        num//=10
    if dup==rem:
        return 'armstrong'
    return 'not armstrong'
print(is_armstrong(153,153))
print('-'*30)

def is_disarm(num,dup,rem=0):
    count=len(str(num))
    while num != 0:
        ld=num%10
        rem=rem+ld**count
        num//=10
        count-=1
    if dup==rem:
        return 'disarm'
    return 'not'
print(is_disarm(135,135))
print('-'*30)

def harshad(num,dup,rem=0):
    while num!=0:
        ld=num%10
        rem+=ld
        num//=10
    if dup%rem==0:
        return 'harshad'
    return 'not'
print(harshad(24,24))
print('-'*30)

def fact(num,mul=1):
    for val in range(1,num+1):
        mul*=val
    return mul
def square(num,copy,dsum=0):
    while num!=0:
        ld=num%10
        dsum+=fact(ld)
        num//=10
    return copy==dsum
def special(num):
    return square(num,num)
num=145
print('special' if special(num) else 'not')
print('-'*30)

def happy(num,rem=0):
    while num!=0:
        ld=num%10
        rem+=ld**2
        num//=10
    return rem
def digit(num):
    while num>9:
        num=happy(num)
    return num==1 or num==7
num=68
print('happy' if digit(num) else 'not')
print('-'*30)
def facinating(num):
    check=(str(num)+str(num*2)+str(num*3))
    for val in range(1,10):
        if str(val) not in check:
            return False
        return True
num=192
print('facinating' if facinating(num) else 'not')
print('-'*30)
def prime(num):
    for val in range(2,num//2+1):
        if num%val==0:
            return False
        return True
def rev(num,dup,rem=0):
    while num!=0:
        ld=num%10
        rem=rem*10+ld
        num//=10
    return rem
num=17
revnum=rev(num,num)
print('emirp' if prime(num)and prime(revnum)and num!=rev(num,num) else 'not')
print('-'*30)

print((lambda v1,v2,v3:v1+v2+v3)(11,55,66))        
print('-'*30)
var=lambda a,b,c:a+b+c
print(var(11,22,33))
print('-'*30)     
def even(num):
    if num%2==0:
        return True
    return False
print(list(map(even,range(10,20))))
print('-'*30)  

p1=[1,2,3,4]
p2=[3,4,5,6]
print(list(map(lambda p1,p2:p1+p2 ,p1,p2)))
print('-'*30)  

print('\n'.join(list(map(lambda a1:'*'*a1,range(1,5)))))
print('-'*30)
print('\n'.join(list(map(lambda a1:'*'*a1,range(5,0,-1)))))
print('-'*30)
print('\n'.join(list(map(lambda sp,st:' '*sp+'*'*st,range(3,-1,-1),range(1,5)))))
print('-'*30)
print('\n'.join(list(map(lambda sp,st:' '*sp+'*'*st,range(5),range(5,0,-1)))))
print('-'*30)
print('\n'.join(list(map(lambda a1:str(a1)*a1,range(5,0,-1)))))
print('-'*30)
def prime(num):
    for fa in range(2,num//2+1):
        if num%fa==0:
            return False
        return True
print(list(filter(prime,range(1,101))))
print('-'*30)
def happy(num):
    while num>9:
        dsum=0
        while num != 0:
            ld=num%10
            dsum+=ld**2
            num//=10
        num=dsum
    return num==1 or num==7
print(list(filter(happy,range(1,101))))
print('-'*30)

from functools import reduce
print(reduce(lambda a1,a2:a1*a2,range(1,6)))
print('-'*30)
#linear search
l=[12,1,3,4,23]
user=23
for val in range(len(l)):
    if l[val]==user:
        print(val)
        break
else:
    print(-1)
print('-'*30)
#binery search
l=[12,1,3,4,23]
user=23
low=0
high=len(l)-1
while low<=high:
    mid=(low+high)//2
    if l[mid]>user:
        high=mid-1
    elif l[mid]<user:
        low=mid+1
    elif l[mid]==user:
        print(mid)
        break
else:
    print(-1)
print('-'*30)
#interpolation search
l=[10,22,25,49,53,420]
user=49
low=0
high=len(l)-1
while (low<=high) and (l[low]<=user<=l[high]):
    ind=int(low+((low-high)/(l[low]-l[high]))*(user-l[low]))
    if l[ind] > user:
        high = ind-1
    elif l[ind] < user:
        low = ind+1
    elif l[ind] == user:
        print(ind)
        break
else:
    print(-1)
    
#sorting technics
#1.bubble sort
l=[8,4,5,2,55]
for ind1 in range(len(l)-1,0,-1):
    for ind2 in range(ind1):
        if l[ind2]>l[ind2+1]:
            l[ind2],l[ind2+1]=l[ind2+1],l[ind2]
print(l)
print('-'*30)
#2.selection sort
l=[2,4,1,55,3]
for ind1 in range(len(l)-1):
    lowind=ind1
    for ind2 in range(ind1+1,len(l)):
        if l[lowind]>l[ind2]:
            lowind=ind2
    l[ind1],l[lowind]=l[lowind],l[ind1]
print(l)
print('-'*30)           
#3.Quick sort:
l=[2,4,1,55,3]
def quick(l):
    if len(l)<=1:
        return l
    pivot=l[0]
    low=[l[ind] for ind in range(1,len(l)) if pivot>l[ind]]
    high=[l[ind] for ind in range(1,len(l)) if pivot<l[ind]]
    return quick(low)+[pivot]+quick(high)
print(quick(l))
print('-'*30)
#4.merge sort:
def conquer(mlist,llist,rlist):
    mind,lind,rind=0,0,0
    while lind<len(llist) and rind<len(rlist):
        if llist[lind]>rlist[rind]:
            mlist[mind]=rlist[rind]
            rind+=1
            mind+=1
        else:
            mlist[mind]=llist[lind]
            lind+=1
            mind+=1
    while lind<len(llist):
        mlist[mind]=llist[lind]
        mind+=1
        lind+=1
    while rind<len(rlist):
        mlist[mind]=rlist[rind]
        mind+=1
        rind+=1
def divide(l):
    if len(l)>1:
        left,right=l[:len(l)//2],l[len(l)//2:]
        divide(left)
        divide(right)
        conquer(l,left,right)
l=[12,1,3,4,23]
divide(l)
print(l)
print('-'*30)

lines=5
for line in range(1,lines+1):
    for star in range(line):
        if (star==0)or(line==lines) or (star==line-1):
            print('*',end='')
        else:
            print(' ',end='')
    print()
print('-'*30)
n=5
for line in range(n,0,-1):
    for star in range(line):
        if (star==0)or(line==n)or(star==line-1):
            print('*',end='')
        else:
            print(' ',end='')
    print()
print('-'*30)
n=5
spaces=n-1
for line in range(1,n+1):
    for sp in range(spaces):
        print(' ',end=' ')
    for star in range(line):
        if (star==0)or(line==n)or (star==line-1):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    spaces-=1
    print()
print('-'*30)
n=5
spaces=0
for line in range(n,0,-1):
    for sp in range(spaces):
        print(' ',end=' ')
    for star in range(line):
        if (star==0) or (star==line-1) or (line==n):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    spaces+=1
    print()
print('-'*30)
n=5
for row in range(n):
    for col in range(n):
        if (row==col) or(row+col==n-1):
            print('*',end='')
        else:
            print(' ',end='')
    print()
print('-'*30)
n=5
spaces=n-1
star=1
for row in range(1,n+1):
    for sp in range(spaces):
        print(' ',end=' ')
    for st in range(star):
        if (st==0)or(st==star-1)or(st==(n*2)-1):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
    spaces-=1
    star+=2
print('-'*30)

n='India is my country'
s=''
for ind in range(len(n)-1,-1,-1):
    s+=n[ind]
print(s)

print('-'*30)
n='India is my country'
s=''
n1=n.split()
for ind1 in range(len(n1)-1,-1,-1):
    s+=n1[ind1]+' '
print(s)
print('-'*30)

n='India is my country'
s=''
n1=n.split()
for ind1 in range(len(n1)):
    n2=n1[ind1]+' '
    for ind2 in range(len(n2)-1,-1,-1):
        s+=n2[ind2]
print(s)
print('-'*30)'''


n='3a5b0c5p'
res=''
for val in range(len(n)):
    if '0'<=str(n[val])<='9':
        res+=int(n[val])*(n[val+1])
print(res)
        
    












   
    
    
        
   
        





















     
    
