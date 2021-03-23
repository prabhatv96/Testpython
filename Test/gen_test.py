def new(dict):
    for k,v in dict.items():
        yield k,v
d={1:"hello",2:"world"}
obj=new(d)
print(obj)
# print(next(obj))
for i in obj:
    print(i)

