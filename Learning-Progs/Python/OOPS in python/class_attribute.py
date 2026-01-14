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