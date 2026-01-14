# python code for implementing Rail Fence Cipher
def railfence(string):
    result = ""
    #Defines a function railfence() that takes a parameter txt (the text to encrypt).
    # Initializes result as an empty string — this will hold the final ciphertext.
    
    for i in range(len(string)):
        if i % 2 == 0:
            result += string[i]
        #Loops through each character using its index i.
        # i % 2 == 0 → selects even indices (0, 2, 4 …).
        # Adds characters at even positions to result.
        
    for i in range(len(string)):
        if i % 2 != 0:
            result += string[i]
        #Loops again through each character.
        # i % 2 != 0 → selects odd indices (1, 3, 5 …).
        # Adds characters at odd positions to the end of result.
    return result

string = input("Enter the text to encrypt: ")
# Reads user input and stores it in string.
print("Cipher: " + railfence(string))