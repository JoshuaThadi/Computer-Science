'''
Design a program for creating a three consecutive ones
'''

class ThreeConsecutiveOnesMachine:
    def __init__(self):
        self.consecutive_ones = 0
        self.detected = False 
    
    def process_input(self, bit):
        if bit == '1':
            self.consecutive_ones += 1
        else:
            self.consecutive_ones = 0  # Reset counter if '0' appears
            
        if self.consecutive_ones == 3 and not self.detected:
            print("Three consecutive ones detected!")
            self.detected = True  # Ensure it prints only once
            
def main():
    machine = ThreeConsecutiveOnesMachine()
    input_stream = input("Enter your binary string -> ")
    print("Input Stream ->", input_stream)
    
    for bit in input_stream:
        machine.process_input(bit)
        
    if not machine.detected:
        print("Three consecutive ones NOT detected")
        
if __name__ == "__main__":
    main()
