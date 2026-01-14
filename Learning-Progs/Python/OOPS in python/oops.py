# OOPS (object oriented programming)

# 1] Classes 
'''
Classes : In object-oriented programming (OOP) in Python, a class serves as a blueprint for creating objects.
Abstract Class: An abstract class is a special type of class that cannot be instantiated directly.
'''

# Creating a class called Item
class Item:
    def calculate_total_price(self, x, y):
        return x * y
    
item1 = Item()
item1.name = "Phone"
item1.price = 100
item1.quantity = 5
print(item1.calculate_total_price(item1.price, item1.quantity))

item2 = Item()
item2.name = "Laptop"
item2.price = 1000
item2.quantity = 3
print(item2.calculate_total_price(item2.price, item2.quantity))


# 2] Constructor __init__
''' 
In Python, __init__ is a special method, also known as the initializer or constructor, that is automatically invoked when a new instance (object) of a class is created. 

Instance Attribute -> A instance attribute in Python is a variable that is specific to a particular instance (object) of a class. This means that each object created from a class will have its own independent copy of the instance attributes, and changing the value of an instance attribute in one object will not affect other objects of the same class. 
'''
class Item:
    def __init__(self, name, price, quantity): # self -> initializes the name attribute
        self.name = name # -> this is called as "instance attribute"
        self.price = price
        self.quantity = quantity
    
    def calculate_total_price(self):
        return self.price * self.quantity
    
# create instances of item
item1 = Item("Phone", 500, 5)
item2 = Item("Laptop", 1000, 3)
print(item1.name, item1.price, item1.quantity) 
print(item2.name, item2.price, item2.quantity)
print(item1.calculate_total_price())
print(item2.calculate_total_price())


# to strictly specify the data type of the parameter 
class Item:
    # specifing the data type
    def __init__(self, name:str, price:float, quantity:int):
        self.name = name
        self.price = price
        self.quantity = quantity
    
    def calculate_total_price(self):
        return self.price * self.quantity

item1 = Item("Phone", 500, 5)
item2 = Item("Laptop", 1000, 3)
print(item1.name, item1.price, item1.quantity) 
print(item2.name, item2.price, item2.quantity)
print(item1.calculate_total_price())
print(item2.calculate_total_price())


# Assert statement
'''
In Python, the assert statement is a debugging tool used to test assumptions about your code. It acts as a sanity check that verifies whether a certain condition holds true during program execution. 
'''
class Item:
    # specifing the data type
    def __init__(self, name:str, price:float, quantity:int):

        # run validations to the received arguments
        assert price >= 0, f"Price {price} is not greater than 0."
        assert quantity >= 0, f"Quantity {quantity} is not greater than 0."
        
        # assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity
    
    def calculate_total_price(self):
        return self.price * self.quantity
    
item1 = Item("Phone", 500, 5)
item2 = Item("Laptop", 1000, 3)
print(item1.name, item1.price, item1.quantity) 
print(item2.name, item2.price, item2.quantity)
print(item1.calculate_total_price())
print(item2.calculate_total_price())


# Class Attribute
'''
Class Attribute -> A class attribute in Python is a variable that is owned by the class itself, rather than by individual instances (objects) of the class. This means that all instances of a class will share the same value for a particular class attribute.

__dict__ -> The __dict__ attribute is a built-in attribute of Python objects that stores the object's writable attributes. It is a dictionary-like object that contains all the attributes (both instance and class attributes) of the object.

In Python, __dict__ is a special attribute that every object (including instances of classes, classes themselves, functions, modules, and more) possesses. It serves as a namespace, storing the object's attributes in the form of a dictionary, where attribute names are the keys and their corresponding values are the dictionary's values. 

In Python, the .items() method is a built-in dictionary method that returns a view object containing all the key-value pairs of a dictionary as tuples. Each tuple in the view object represents a single key-value pair, with the key as the first element and the value as the second. 

'''

class Item:
    
    # class Attribute
    pay_rate = 0.8 # the pay rate after 20% discount
    
    def __init__(self, name:str, price:float, quantity:int):
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self):
        return self.price * self.quantity
    
    def apply_discount(self):
        self.price = self.price * self.pay_rate # Item.pay_rate, strictly passes the actual class attribute value

item1 = Item("Phone", 500, 5)
item1.apply_discount() # the pay_rate will be accessed from the class only
print(f"Total price after discount for {item1.name}: {item1.price}")

item2 = Item("Laptop", 1000, 3)
# the pay_rate can be overridden by changing it outside the class by applying self to the pay_rate in the apply_discount method
item2.pay_rate = 0.7 
item2.apply_discount()
print(f"Total price after discount for {item2.name}: {item2.price}")

# using __dict__ for accessing instance attributes
print("Item 1 attributes:")
for key, value in item1.__dict__.items():
    print(f"  {key}: {value}")

print("Item 2 attributes:")
for key, value in item2.__dict__.items():
    print(f"  {key}: {value}")


'''
The __repr__ method in Python is a special method (also known as a "dunder" or magic method due to its double underscores) that's designed to return an unambiguous and developer-focused string representation of an object. 
'''

class Item:
    
    all = [] # class attribute to store all instances, initialized as an empty list
    
    # class Attribute
    pay_rate = 0.8 # the pay rate after 20% discount
    
    def __init__(self, name:str, price:float, quantity:int):
        self.name = name
        self.price = price
        self.quantity = quantity
        
        # Actions to execute
        Item.all.append(self)

    def calculate_total_price(self):
        return self.price * self.quantity
    
    def apply_discount(self):
        self.price = self.price * self.pay_rate # Item.pay_rate, strictly passes the actual class attribute value

    def __repr__(self):
        return f"Item({self.name}, {self.price}, {self.quantity})"

item1 = Item("Phone", 500, 5)
item2 = Item("Laptop", 1000, 3)
item3 = Item("Tablet", 300, 7)
item4 = Item("Monitor", 1500, 2)
item5 = Item("Keyboard", 100, 10)

print(Item.all)  # This will print all the items created
for instance in Item.all:
    print(f"Item: {instance.name}, Price: {instance.price}, Quantity: {instance.quantity}")
    
    
# 3] Class Methods vs Static Methods
'''
In Python, class methods and static methods are alternative ways to define functions within a class, offering different levels of interaction with the class and its instances. They are distinct from regular instance methods, which are the most common type and operate on an instance of the class.
'''

'''
1. Class methods
Bound to the class: A class method is associated with the class itself, not with specific instances (objects) of the class.

Decorator: You use the @classmethod decorator to define a class method.
First argument (cls): Class methods automatically take the class itself as their first argument, conventionally named cls. This argument refers to the class to which the method belongs.

Access to class state: Class methods can access and modify class-level attributes (variables) using the cls parameter. They can also call other class methods within the same class.
'''

'''
2. Static methods
Not bound to the class or instance: Static methods are essentially regular functions conceptually grouped within a class, but they don't depend on the class or its instances.

Decorator: You use the @staticmethod decorator to define a static method.
No special first argument: Static methods do not automatically receive self (the instance) or cls (the class) as their first parameter.

Limited Access: They cannot directly access or modify class or instance attributes without those attributes being explicitly passed in as arguments.
'''

import csv
class Item:
     all = []
     pay_rate = 0.8
     
     def __init__(self, name:str, price:float, quantity:int):
         self.name = name
         self.price = price
         self.quantity = quantity
         
         Item.all.append(self)
         
     def calculate_total_price(self):
         return self.price * self.quantity
     
     def apply_discount(self):
         self.price = self.price * self.pay_rate
         
     @classmethod # class method 
     def instantiate_from_csv(cls):
         with open('items.csv', 'r') as f:
             reader = csv.DictReader(f)
             items = list(reader)
             
         for item in items:
             print(item)
             
             # Item or cls can be used to create instance
             Item(
                 name = item.get('name'),
                 price = float(item.get('price')),
                 quantity = int(item.get('quantity')),
             )
    
     @staticmethod # static method
     def is_integer(num):
         # we will count out the floats that are point zero
         # for i.e, 5.0, 10.0
         if isinstance(num, float):
             return num.is_integer()
         elif isinstance(num, int):
             return True
         else:
             return False
         
     def __repr__(self):
         return f"Item({self.name}, {self.price}, {self.quantity})"

print(Item.instantiate_from_csv()) # This will print all the items created
print(Item.is_integer(5.9))
print(Item.all)


# Inheritance
'''
inheritance is a mechanism that allows a class (called a child or derived class) to inherit properties and methods from another class (called a parent or base class). This promotes code reusability and creates a hierarchical relationship between classes. Essentially, the child class gets a "head start" by inheriting the features of the parent class and can then add its own unique characteristics. 
'''

