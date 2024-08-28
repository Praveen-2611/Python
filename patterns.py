var=4
num=var
spaces=var-1
for line in range(1,var+1):
    print(' '*spaces,end='')
    for num in range(line):
        print(line,end='')
    spaces-=1
    print()
    
    
