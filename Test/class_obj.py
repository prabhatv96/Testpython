class Parent():
    def __init__(self,n,age):
        self.name=n
        self.age=age

obj=Parent("Ram",100)
print(obj.name,obj.age)

class Child(Parent):
    def __init__(self,n,age,s):
        Parent.__init__(self,n,a)
        self.std=s

cobj=Child("ak",50,"classic")
print(cobj.name,cobj.age,cobj.std)