while True:
    i,j = map(int,input("Enter values for i and j---> ").split())
    mx_cycle_len = 0


    for n in range(i,j):
        cycle_len = 1
        while n>1:
            if n%2==0:
                n/=2
            else:
                n=3*n+1
            cycle_len+=1
            
        if cycle_len > mx_cycle_len:
            mx_cycle_len = cycle_len
            
    if i!=0 and j!=0:
        pass
    else:
        break
    print(i,j,mx_cycle_len)
    
    
        
