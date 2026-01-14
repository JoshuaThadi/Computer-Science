# *args and **kwargs
'''
*args and **kwargs are used in function definitions to handle a flexible number of arguments when the exact count isn't known beforehand. They offer great flexibility and versatility, making your functions adaptable to different argument scenarios without explicitly defining each one.
'''

# example for *args
def my_sum(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total

print(my_sum(1, 2, 3))    # Output: 6
print(my_sum(10, 20, 30, 40)) # Output: 100


# example for **kwargs
def create_user(**user_details):
    print("User details:")
    for key, value in user_details.items():
        print(f"{key}: {value}")

create_user(name="Alice", age=30, city="New York") 
# Output:
# User details:
# name: Alice
# age: 30
# city: New York


# example of both the combination
def combined_arguments(a, b, *args, **kwargs):
    print(f"Fixed arguments: a={a}, b={b}")
    print(f"Positional arguments: {args}")
    print(f"Keyword arguments: {kwargs}")

combined_arguments(1, 2, 3, 4, name="John", role="Developer")
# Output:
# Fixed arguments: a=1, b=2
# Positional arguments: (3, 4)
# Keyword arguments: {'name': 'John', 'role': 'Developer'}
