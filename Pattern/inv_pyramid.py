n=int(input("Enter number of lines: "))
k=2
for i in range(n,-1,-1):
    print(end=" "*k)
    for j in range(i):
        print("*",end=" ")
    k=k+1
    print("\r")