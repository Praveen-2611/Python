rev=0
n=154
while n!=0:
    rem=n%10
    rev=(rev*10)+rem
    n//=10
print(rev)
    
