# A python program to illustrate Caesar Cipher Technique
def encrypt(text, s):
    result = " "
    # text → the message you want to encrypt.
    # s → the number of positions to shift (the key).
    # result is initialized as an empty string (it will store the encrypted text).
    
    # traverse text
    for i in range(len(text)):
        char = text[i]
        # A loop goes through each character in the text using its index.
        # char represents the current character being processed.
        
        # Encrypt uppercase characters
        if (char.isupper()):
            result += chr((ord(char) + s - 65) % 26 + 65)
            # char.isupper() checks if the character is uppercase (A–Z).
            # ord(char) converts the letter into its ASCII value.
            # Example: ord('A') = 65
            
            # ord(char) - 65 → converts A–Z to 0–25
            # + s → adds the shift value
            # % 26 → wraps around if it goes past ‘Z’
            # + 65 → converts back to the ASCII range for uppercase letters
            # chr() converts the number back to a letter.
            # Then the letter is added to result.
            
        # Encrypt lowercase characters
        else:
            result += chr((ord(char) + s - 97) % 26 + 97)
            #This part runs if the character is lowercase (a–z).
            # Similar logic:
            # ord('a') = 97
            # (ord(char) + s - 97) % 26 + 97 ensures the shift wraps from ‘z’ to ‘a’.
            # Adds the encrypted lowercase letter to result.
    return result

#check the above function
text = input("Enter the text to encrypt: ")
s = int(input("Enter the shift number: "))
print("Text : " + text)
print("Shift : " + str(s))
print("Cipher: " + encrypt(text, s))