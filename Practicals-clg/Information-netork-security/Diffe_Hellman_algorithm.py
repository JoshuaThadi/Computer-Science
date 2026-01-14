# Python code for implementing Diffie-Hellman Algorithm 
# Diffie-Hellman Algorithm

# The Diffie-Hellman (DH) algorithm is a cryptographic key exchange protocol that allows two parties to securely share a secret key over an insecure channel without transmitting the key itself.

# It is not used for encrypting messages directly — it is used to generate a shared secret key for symmetric encryption.

from random import randint 
if __name__ == '__main__': 
    P = 23 
    G = 9 
    print('The Value of P is :%d'%(P)) 
    print('The Value of G is :%d'%(G)) 
    # P → a prime number, used as the modulus.
    # G → generator (primitive root modulo P), used for exponentiation.
    # Both P and G are public parameters
    
    a = 4 
    print('Secret Number for Alice is :%d'%(a)) 
    # a → Alice’s private key (kept secret).
    # Here, it’s hardcoded as 4.
    
    x = int(pow(G,a,P))  
    # x = G^a mod P → Alice’s public key.
    # pow(G, a, P) computes (G ** a) % P efficiently.
    # For this example: x = 9^4 mod 23 = 9*9*9*9 % 23 = 6561 % 23 = 6
    # x is sent to Bob.
    
    b = 6 
    print('Secret Number for Bob is :%d'%(b)) 
    y = int(pow(G,b,P))  
    # b → Bob’s private key, hardcoded as 6.
    # y = G^b mod P → Bob’s public key.
    # y = 9^6 mod 23 = 531441 % 23 = 2
    # y is sent to Alice.
    
    ka = int(pow(y,a,P)) 
    kb = int(pow(x,b,P)) 
    print('Secret key for the Alice is : %d'%(ka)) 
    print('Secret Key for the Bob is : %d'%(kb))