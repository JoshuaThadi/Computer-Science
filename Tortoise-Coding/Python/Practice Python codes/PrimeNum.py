# program to check if a number is prime or not

# method 1
num = 11
# Negative numbers, 0 and 1 are not primes
if num > 1:
  
    # Iterate from 2 to n // 2
    for i in range(2, (num//2)+1):
      
        # If num is divisible by any number between
        # 2 and n / 2, it is not prime
        if (num % i) == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")
else:
    print(num, "is not a prime number")


#method 2
while True:
    try:
        user_input = input("Enter the number or type 'exit' to quit -> ")
        if user_input.lower() == "exit":
            break

        num = int(user_input)
        # define a flag variable
        is_Prime = False

        if num == 0 or num == 1:
            print(num, "is not a prime number")
        elif num > 1:
            # check for factors
            for i in range(2, num):
                    if num % i == 0:
                        # if factor is found, set flag to True
                        is_Prime = True
                        # break out of loop
                        break

            # ckeck if flag is True
            if is_Prime:
                print(num, "is not a prime number")
            else:
                print(num, "is a prime number")

            print(f"\nPrime numbers from 2 to {num}")    
            for i in range(2, num):
                for x in range(2, i):
                    if i % x == 0:
                        break
                else:
                    print(i, "is a prime number")

    except ValueError:
        print("Invalid input")

