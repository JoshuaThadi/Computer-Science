'''
Design a program for accepting decimal number divisible by 2
'''

class DFA:
    def __init__(self):
        self.state = 0
        
    def is_divisible(self, input_s):
        for digit in input_s:
            if digit not in ('1', '0'):
                return False 
            self.state = (self.state*2+int(digit)) % 2
        return self.state == 0
    
def main():
    dfa = DFA()
    while True:
        try:
            binary_num = input("Enter a binary number -> ")
            if not binary_num:
                print("Invalid/empty input, only binary string accepted.")
                continue 
            if dfa.is_divisible(binary_num):
                print("The number is divisble by 2.")
            else:
                print("The number is not divisble by 2.")
        except KeyboardInterrupt:
            print("\nProgram Terminated")
            break 
        
if __name__ == "__main__":
    main()
