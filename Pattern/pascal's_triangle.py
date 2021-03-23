n=int(input("Enter the maximal number: "))
def function(n,k):
    res=1
    if(k>n-k):
        k=n-k
    for i in range(0,k):
        res=res*(n-i)
        res=res//(i+1)
    return res
for i in range(n):
    for j in range(i+1):
        print(function(i,j)," ",end=" ")
    print()
