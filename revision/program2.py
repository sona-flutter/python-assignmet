row=4
for i in range(row):
    print(" " * (2*(row-i-1)),end=" ")
    for j in range(1,i+2):
        print(j,end=" ")
        
    for j in range(i,0,-1):
        print(j,end=" ")
    print()
    
for i in range(row):
    print(" " *(2*i),end=" ")
    
    for j in range(1,row-i+1):
        print(j,end=" ")
    for j in range(row-i-1,0,-1):
        print(j,end=" ")
    print()