def prime(num,n=2):
    if n==num//2+1:
        return 0
    return (num%n==0)+prime(num,n+1)
def pali(num,count):
    if num==0:
        return 0
    return((num%10)*(10**(count-1))+pali(num//10,count-1))
num=17
revnum=pali(num,len(str(num)))

print('emirp' if prime(num)==1 and prime(revnum)==1 and  num != revnum else 'not')
                
 
