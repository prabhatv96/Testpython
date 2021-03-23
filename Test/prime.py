a,b=map(int,input().split())
l=[]
for i in range(b,1,-1):
    if i>1:
        for j in range(2,i):
            if(i % j==0):
                break
        else:
            l.append(i)
            break
if a<0:
    for i in range(-a,1,-1):
        if i>1:
            for j in range(2,i):
                if(i % j==0):
                    break
            else:
                l.append(i)
                break
    s=l[0]-l[1]
    print(s)
else:
    for i in range(a,b):
        if i > 1:
            for j in range(2, i):
                if (i % j == 0):
                    break
            else:
                l.append(i)
                break
    print(sum(l))
