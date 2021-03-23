l=lambda a:a*2
print(l(5))

#map
lst=[1,2,3,4,5]
lst1=list(map(lambda x: x**2,lst))
print(lst1)

#reduce
from functools import reduce
r=reduce(lambda a,b: a+b,[1,2,3,4,5])
print(r)