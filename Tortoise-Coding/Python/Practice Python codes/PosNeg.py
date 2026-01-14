# program to check if a number is negative or positive

check = int(input("Enter a number : "))
if (check == 0):
    print("Zero")
elif (check > 0):
    print('The number %0.1f is positive' %(check))
elif (check < 0):
    print('The number %0.1f is negative' %(check))
else :
    print('Input is Invalid')

