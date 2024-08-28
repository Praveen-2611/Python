rev=0
n=151
copy=n
while n!=0:
    rem=n%10
    rev=(rev*10)+rem
    n//=10
if copy==rev:
    print(f'{copy} is palindrome')
else:
    print(f'{copy} is not palindrome')
