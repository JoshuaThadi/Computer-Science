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
