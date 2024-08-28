num=327
check=(str(num)+str(num*2)+str(num*3))
def fa(num,n=1,f=0):    
    if n > 9:
        return 0
    if str(n) in check:
        return fa(num,n+1)+(f+1)
    return False
print("fa" if fa(num)==9 else "not")
