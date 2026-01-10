# class Student:
#     subject="Mathematics"
#     college="ABC College"
#     year=2024

# stu1= Student()
# stu2= Student()
# print(stu1.subject,stu1.college,stu1.year)
# print(stu2.subject,stu2.college,stu2.year)

# class Student:  #parameterized constructor
#     def __init__(self, name, age, grade):
#         self.name = name
#         self.age = age
#         self.grade = grade

#     def get_name(self):    #default constructor
#         return self.name

# stu1=Student("Alice",20,"A")
# stu2=Student("Bob",22,"B")
# print(stu1.name,stu1.age,stu1.grade)
# print(stu2.name,stu2.age,stu2.grade)

# print(f"{stu1.name} is the name of {stu1.get_name()}")

# for one class only one init method no multiple constructore but allowed in java and cpp

# class Student:
#     colege_name="ABC College" #class 
#     def __init__(self, name, age, grade):
#         self.name = name  #instance
#         self.age = age
#         self.grade = grade

# stu1=Student("Alice",20,"A")

# print(stu1.name)  #instance attribute can be acessed only by objects
# print(stu1.colege_name)
# print(Student.college_name)  #  class attribute can be acessed by object as well as class name 

# class Student:
#     college_name="ABC College" #class 
#     PI=3.14
#     def __init__(self, name, age, grade):
#         self.name = name  #instance
#         self.age = age
#         self.grade = grade
#         self.PI=3

# stu1=Student("Alice",20,"A")
# print(stu1.PI)  #instance attribute
# print(Student.PI)  #class attribute


# class Laptop:
#     storage_type="SSD" #class attribute
#     def __init__(self, brand, ram, storage):
#         self.brand = brand  #instance attribute
#         self.ram = ram
#         self.storage = storage
#     @classmethod  #this decorater is used to define class method changes the functions behaviour   
#     def get_storage_type(cls):
#         print(f"storage type is {cls.storage_type}")

#     @staticmethod  #this decorater is used to define static method  
#     def calc_discount(price,discount):
#         print(f"dicounted rice is {price-(price*discount/100)}")
    
#     def get_info(self):
#         print(f"laptop has{self.ram}GB RAM and {self.storage}GB {self.storage_type} storage")

# l1=Laptop("Dell",16,512)
# l1.get_info()
# l2=Laptop("HP",8,256)
# l2.get_info()

# l1.get_storage_type()
# Laptop.get_storage_type()

# l1.calc_discount(50_000,10)

# class methods can access only class attributes not instance attributes


# class Products:
#     count = 0  #class attribute


#     def __init__(self,name,price,quantity):
#           self.name = name
#           self.price = price
#           self.quantity = quantity
#           Products.count += 1
    
#     @classmethod
#     def get_count(cls):
#         print(f"Total products: {cls.count}")   
            

#     @staticmethod
#     def calc_discount(price,discount):
#         print(f"discounted price is{price-(price*discount/100)}")

# p1= Products("phone",20000,2)
# print(p1.name,p1.price,p1.quantity)
# p1.calc_discount(20000,5)

# p2= Products("laptop",50000,1)
# print(p2.name,p2.price,p2.quantity)
# Products.get_count()



# class BankAccount:
#     def __init__(self,name,balance):
#         self.name = name #public 
#         self.__balance = balance #private - data mangling 
    
#     def get_balance(self): #getter method
#         return self.__balance
#     def  set_balance(self,newBalance):
#         self.__balance = newBalance


# acc1 = BankAccount("John",100_000)

# acc1.set_balance(150_000)

# print(acc1.get_balance())
# print(f"Account holder name is {acc1.name} and balance is {acc1.get_balance()}")


# class Employee:
#     start_time="10 am"
#     end_time="6 pm"

#     def change_time(self,new_end_time):
#         self.end_time = new_end_time

# class Teacher(Employee):
#         def __init__(self,subject):
#             self.subject = subject

# class AdminStaff(Employee):
#         def __init__(self,department):
#             self.department = department

# class  Accountant(Employee):
#         def __init__(self,salary):
#             self.salary= salary


# t1= Teacher("Maths")
# print(t1.start_time)
# t1.change_time("5 pm")

# print(f"{t1.subject} ends at {t1.end_time}")


#abstraction 

# from abc import ABC

# class Animal(ABC):
#     @abstractmethod
#     def sound(self):
#         pass
# class Dog(Animal):
#     def sound(self):
#        print("Woof")

# dog = Dog()
# dog.sound()


# # function overriding
# class Vehicle:
#     def start_engine(self):
#         print("type = vehicle")

# class Car(Vehicle):
#     def start_engine(self):
#         print("type = car")

# v1= Car()
# v1.start_engine()



#duck typing

class Teacher():
    def get_designation(self):
        return "Teacher"
    
class Student():
    def get_designation(self):
        return "Student"

t1= Teacher()
s1= Student()
print(t1.get_designation())
print(s1.get_designation()) 
