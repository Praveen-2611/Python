var=4
num=var
spaces=var-1
for line in range(1,var+1):
    print(f"{' '*spaces}{str(line)}",end='')
    spaces-=1
    num+=1
    print()
