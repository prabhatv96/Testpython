n=int(input("Enter number of lines: "))
k=n*2-2
for i in range(n):
    print(end=" "*k)
    print("* "*(i+1))
    k=k-2
for i in range(n,-1,-1):
    print(end=" "*(k+4))
    print("* "*(i-1))
    k=k+2
