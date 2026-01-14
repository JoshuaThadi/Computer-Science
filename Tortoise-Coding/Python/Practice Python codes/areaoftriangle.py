# method 1
a = 5; b = 6; c = 7
s = (a + b + c) / 2
area = (s*(s - a)*(s - b)*(s - c)) ** 0.5
print('The area of a triangle is %0.2f' %area)

# method 2
def area_triangle(base, height):
    a = (1/2)*base*height
    print('Area of a triangle is %0.2f' %a)
b = 3; h = 4
area_triangle(b,h)
