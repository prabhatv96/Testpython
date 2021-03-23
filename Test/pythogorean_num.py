from math import sqrt
n=int(input("Enter the maximal number: "))
for a in range(1,n+1):
    for b in range(a,n):
        c=a**2 + b**2
        if c-(sqrt(c)**2)==0:
            print(a,b,c)