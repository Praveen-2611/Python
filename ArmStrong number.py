ans=0
n=153
copy=n
count=len(str(154))
while n!=0:
    rem=n%10
    ans=ans+rem**count
    n//=10
if copy==ans:
    print('armStrong')
else:
    print('not')
