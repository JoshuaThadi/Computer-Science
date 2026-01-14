# 1] Add, Sub, Div and mul of two complex numbers.

a = complex(input("Enter the 1st complex number : "))
b = complex(input("Enter the 2nd complex number : "))

print("Given Complex no.are \n 1.", a, "\n 2.", b);
print("Addition of 2 complex no : ", a, " + ", b, " = ", a + b);
print("Subtract of 2 complex no : ", a, " - ", b, " = ", a - b);
print("Multiplication of 2 complex no : ", a, " x ", b, " = ", a * b);
print("Division of 2 complex no : ", a, " / ", b, " = ", a / b, "\n");


# 2] Display the conjugate of a complex number.

a = complex(input("Enter 1st complex no : "));
b = complex(input("Enter 2nf complex no : "));
print("The conjugate of a given number are \n 1.", a.conjugate(),"\n2.", b.conjugate())

# 3] Ploting a set of complex numbers

import matplotlib.pyplot as plt
s = {3 + 3j, 2 + 1j};
x = [x.real for x in s]
y = [x.imag for x in s]
plt.plot(x, y, 'ro')
plt.axis([-6, 6, -6, 6])
plt.show()

# 4] Creating new plot by rotating the given number by 90, 180, 270, and also by scaling a number
#    a = 1/2, a = 1/3, a = 2, etc.

# import matplotlib.pyplot as plt
s = {3 + 3j, 2 + 1j, 3 + 2j}
angle = int(input("Enter Angle : "));
if angle == 90:
    s1 = {x * 1j for x in s}
    print(s1)
    x = [x.real for x in s1]
    y = [x.imag for x in s1]
    plt.plot(x, y, 'ro')
    plt.axis([-6, 6, -6, 6])
    plt.show();
elif angle == 180:
    s1 = {x - 1 for x in s}
    print(s1)
    x = [x.real for x in s1]
    y = [x.imag for x in s1]
    plt.plot(x, y, 'ro')
    plt.axis([-6, 6, -6, 6])
    plt.show();
elif angle == 270:
    s1 = {x * -1j for x in s}
    print(s1)
    x = [x.real for x in s1]
    y = [x.imag for x in s1]
    plt.plot(x, y, 'ro')
    plt.axis([-6, 6, -6, 6])
    plt.show();
else:
    print("Invalid Angle");
    
