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