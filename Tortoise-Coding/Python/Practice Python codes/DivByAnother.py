# python program to find Numbers divisibe by another number 

# METHOD 1
'''Take a list of numbers'''
my_list = [12, 45, 65, 54, 102, 339, 221]

'''use anonymous function to filter'''
result = list(filter(lambda x : (x % 13 == 0), my_list))
print("Numbers divisible by 13 are", result, "\n")


# METHOD 2
while True:
    try:
        list_put = input("Enter numbers seperated by space -> ")
        if list_put.lower() == 'exit':
            break

        my_list = list(map(int, list_put.split()))
        '''Use anonymous function to filter'''
        result = list(filter(lambda x : (x % 13 == 0), my_list))
        print("Numbers divisble by 13 are", result)

    except ValueError:
        print("Invalid input. Please enter numbers only")



# METHOD 3
'''code with interval'''
import time 
def find_divisble_numbers():
    my_list = [12, 45, 65, 54, 102, 339, 221]
    result = list(filter(lambda x : (x % 13 == 0), my_list))
    print("Numbers divisble by 13 are", result)

interval = 5
while True:
    find_divisble_numbers()
    time.sleep(interval)



