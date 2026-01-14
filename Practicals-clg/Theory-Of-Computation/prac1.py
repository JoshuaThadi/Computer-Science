class EndsWith101Machine:
    def __init__(self):
        self.state = 'S0'
        
    def process_input(self, bit):
        if self.state == 'S0':
            if bit == '1':
                self.state = 'S1'
        elif self.state == 'S1':
            if bit == '0':
                self.state = 'S2'
            elif bit == '1':
                self.state = 'S1'  # Fixed typo (uppercase 'S1')
        elif self.state == 'S2':
            if bit == '1':
                self.state = 'S3'
            elif bit == '0':
                self.state = 'S2'  # Stay in S2 for consecutive 0s
        elif self.state == 'S3':  # Accepting state
            if bit == '1':
                self.state = 'S1'
            elif bit == '0':
                self.state = 'S2'
                
    def is_accepted(self):
        return self.state == 'S3'
    
def main():
    input_stream = input("Enter a binary string -> ")
    machine = EndsWith101Machine()
    
    for bit in input_stream:
        machine.process_input(bit)
        
    if machine.is_accepted():
        print(f"The input {input_stream} is accepted as (ends with '101')")
    else:
        print(f"The input {input_stream} is rejected as (it does not end with '101')")

if __name__ == "__main__":
    main()
