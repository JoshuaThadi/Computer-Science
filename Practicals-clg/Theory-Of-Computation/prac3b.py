''' 
Design a program for accepting decimal number divisible by 2
'''

def dfa_for_divisiblility_by_2(decimal_num):
    states = {"q0": "Accept", "q1": "Reject"}
    current_state = "q0"
    
    if decimal_num.is_integer():
        if decimal_num % 10 == 0:
            current_state = "q0"
        else:
            current_state = "q1"
            
    if current_state == "q0":
        return f"{decimal_num} is divisible by 2 (Accept)"
    else:
        return f"{decimal_num} is not divisible by 2 (Reject)"
    
try:
    decimal_num = float(input("Enter a decimal number -> "))
    print(dfa_for_divisiblility_by_2(decimal_num))
except ValueError:
    print("Invalid Input")
    
