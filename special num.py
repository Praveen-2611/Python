ans=0
n=145
copy=n
while n!=0:
    rem=n%10
    fact=1
    for p in range(1,rem+1):
        fact=fact*p
    ans+=fact
    n//=10
if copy==ans:
    print('special num')
else:
    print('not')
   
