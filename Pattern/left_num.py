n=int(input("Enter number of lines: "))
k=n*2-2
for i in range(n):
    print(end=" "*k)
    print(str(i+1)*(i+1))
    k=k-1
for i in range(n,-1,-1):
    print(end=" "*(k+2))
    print(str(i-1)*(i-1))
    k=k+1