n=20
while n>9:
    dsum=0
    while n!=0:
        ld=n%10
        dsum=dsum+ld**2
        n//=10
    n=dsum
if n==1 or n==7:
    print('happy')
else:
    print('not')


n=156
copy=n
res=0
while n!=0:
    ld=n%10
    res=res+ld
    n//=10
if copy%res==0:
    print('h')
else:
    print('n')


n=145
copy=n
res=0
while n!=0:
    ld=n%10
    fact=1
    for num in range(1,ld+1):
        fact=fact*num
    res=res+fact
    n//=10
if copy==res:
    print('s')
else:
    print('n')
    
n=13
position=1
res=0
while n!=0:
    ld=n%2
    res=res+ld*position
    position*=10
    n//=2
print(res)


n=1010
res=0
power=0
while n!=0:
    ld=n%10
    res=res+(ld*2**power)
    power+=1
    n//=10
print(res)

n=192
c=str(n)+str(n*2)+str(n*3)
for val in range (1,10):
    if str(val)not in c:
        print('n')
        break
else:
    print('fascinating')

num=6
n=0
while n*(n+1)<=num:
    if n*(n+1)==num:
        print('pronic number')
        break
    n+=1
else:
    print('not')

num=25
n=0
while n*n<=num+1:
    if n*n==num+1:
        print('sunny number')
        break
    n+=1
else:
    print('not')

