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

