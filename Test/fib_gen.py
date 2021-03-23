n=int(input("Limit: "))
def fib():
    f,s=0,1
    while True:
        yield f
        f,s=s,f+s
for i in fib():
    if i>n:
        break
    print(i,end=" ")