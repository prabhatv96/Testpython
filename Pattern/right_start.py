n=int(input("Enter number of lines: "))
for i in range(n):
    print("* "*(i+1))
for i in range(n,-1,-1):
    print("* "*(i-1))