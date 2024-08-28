ans=0
n=135
copy=n
count=len(str(n))
while n!=0:
    rem=n%10
    ans=ans+rem**count
    n//=10
    count-=1
if copy==ans:
    print('disarum')
else:
    print('not')
