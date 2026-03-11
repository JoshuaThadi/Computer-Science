'''
To solve this problem using a list comprehension, you can nest the iterations for (x),
(y), and (z) within a single set of square brackets. 
The condition to filter out coordinates where the sum equals (n) 
is added at the end of the comprehension.

'''

"""
How it works: Ranges: Since the dimensions are inclusive (from (0) to (x)), 
we use range(x + 1).Order: By nesting the loops in the order i, then j, then k, 
the list is automatically generated in lexicographic increasing order.

Filtering: The if (i + j + k) != n clause ensures that only coordinates 
whose sum is not equal to \(n\) are included in the final list.

Efficiency: This approach is more concise than using multiple 
for loops and .append() calls, which is the preferred "Pythonic" way 
to handle such transformations.

"""

if __name__ == '__main__':
    x = int(input("Enter x :"))
    y = int(input("Enter y :"))
    z = int(input("Enter z :"))
    n = int(input("Enter n :"))

    permutation = [[i, j, k] for i in range(x + 1)
                             for j in range(y + 1)
                             for k in range(z + 1)
                             if (i + j + k) != n]
    print(permutation)
