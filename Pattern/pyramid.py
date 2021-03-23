n=int(input("Enter number of lines: "))
k=n
for i in range(n):
    print(end=" "*k)
    for j in range(i+1):
        print("*",end=" ")
    k=k-1
    print("\r")

