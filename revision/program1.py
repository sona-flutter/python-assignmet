row=int(input("Enter the number"))
for i in range(row):
    num=1
    for j in range(i+1):
        print(num,end=" ")
        num+=1
    print()