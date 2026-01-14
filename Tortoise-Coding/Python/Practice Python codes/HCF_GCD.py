'''
The highest common factor (H.C.F) or greatest common divisor (G.C.D) of two numbers 
is the largest positive integer that perfectly divides the two given numbers.
For example, the H.C.F of 12 and 14 is 2.
'''

# python program to find H.C.F of two numbers

def compare_hcf(x, y):
    if x > y:
        smaller = y 

    else:
        smaller = x 

    for i in range(1, smaller + 1):
        if((x % i == 0) and (y % i == 0)):
            hcf = i
    return hcf 

num1 = 54; num2 = 24
print(f"The H.C.F is {compare_hcf(num1, num2)}")

'''
    Euclidean algorithm
This algorithm is based on the fact that H.C.F. of two numbers divides their difference as well.
In this algorithm, we divide the greater by smaller and take the remainder. 
Now, divide the smaller by this remainder.
Repeat until the remainder is 0.
For example, if we want to find the H.C.F. of 54 and 24, we divide 54 by 24.
The remainder is 6. Now, we divide 24 by 6 and the remainder is 0. Hence, 6 is the required H.C.F.
'''

# Funtion to find HCF the using Euclidean algorithm

def compute_hcf(x, y):
    while(y):
        x, y = y, x % y 
    return x 

hcf = compute_hcf(54, 24)
print("The HCF is", hcf)
