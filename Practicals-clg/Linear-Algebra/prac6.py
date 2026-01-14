# a] find the gcd of 2 numbers using Euclid's

import math
a = int(input("Enter a number : "))
b = int(input("Enter another number : "))
print("GCD of ", a, "and", b, "is", math.gcd(a, b))

# b] Enter  a positive Number N & find numbers a & b such that a2 - b2 = N

import math
def find_factors(N):
    factors = []
    for i in range(1, int(math.sqrt(N)) + 1):
        if N % i == 0:
            factors.append(i)
            if i != N // i:
                factors.append(N // i)
    return sorted(factors)  # Corrected 'Sorted' to 'sorted'

def verify_m_and_n(N):
    factors = find_factors(N)
    print(f"Factors of {N} : {factors}")
    for a in factors:  # Changed 'i' to 'a' for clarity
        for b in factors:
            if (a + b) % 2 == 0 and (b - a) % 2 == 0:  # Corrected '&' to 'and'
                m = (a + b) // 2
                n = (b - a) // 2
                if (m**2) - (n**2) == N:
                    print(f"m = {m}, n = {n}, a = {a}, b = {b}")
                    print(f"Verification : {m}^2 - {n}^2 = {m**2} - {n**2} = {N}")
                    return
    print(f"No valid (m, n) pair found for N = {N}")

# Input is expected to be an integer, so convert the input string to an integer
N = int(input("Enter a number N : "))
verify_m_and_n(N)


                    
