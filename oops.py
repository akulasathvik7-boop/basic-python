class sathvik:
    def __init__(self):
        print("iam the consturctor")
        self.num=12
    def add(self,a,b):
        return a+b
    

obj1=sathvik()
obj2=sathvik()
result=obj1.add(2,3)
print(result)
print(obj2.num)