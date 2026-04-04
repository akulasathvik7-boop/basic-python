# class sathvik:
#     def __init__(self):
#         print("iam the consturctor")
#         self.num=12
#     def add(self,a,b):
#         return a+b
    

# obj1=sathvik()
# obj2=sathvik()
# result=obj1.add(2,3)
# print(result)
# print(obj2.num)


# class ABC:
#     def __new__(cls):
#         print("Im the real constuctor")
#         return super().__new__(cls)   

#     def __init__(self):
#         print("iam just is here for only initliazing variables")
#     def add(self):
#         print(f"addition of 2 and 3: {2+3}")

# obj2=ABC.__new__(ABC)
# obj2.add()


#--------------------------------------------------------------------------------------------
#   1.Single inheritance
# class Animal:
#     def eat(self):
#         print("animal will eat")

# class Dog(Animal):
#     def bark(self):
#         print("the dog will bark")

# obj1=Dog()
# obj1.eat()
# obj1.bark()


#--------------------------------------------------------------------------------------------
#  2.mutlilevel inheritance

# class vehicle:
#     def start(self):
#         print("start with pertrol")

# class Audio(vehicle):
#     def features(self):
#         print("iam alos run with disel")

# class audio_lite(Audio):
#     def speed(self):
#         print("speed s faster")

# obj1=audio_lite()
# obj1.speed()
# obj1.features()
# obj1.start()

#ducktyping------------------------------------------------------------------------------
# class Animal:
#     def __init__(self):
#         print("Animal live in forest")

# class Dog(Animal):
#     def bark(self):
#         print("dog barks")

# class Cat(Animal):
#     def meow(self):
#         print("cat says meow meow")

# objects=[Dog(),Cat(),Animal()]

# for i in objects:
#     print(i)


class sathvik:
    def __init__(self,color,age):
        self.age=age
        self.color=color
    def __get__(self):
       print(f"sathvik is {self.color} in color and his age is {self.age}")
x=sathvik('white',24)
x.__get__()