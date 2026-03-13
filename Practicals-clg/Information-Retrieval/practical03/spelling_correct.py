# Spelling_correction.py
# A Naive recursive Python program to find the minimum number of
# operations required to convert str1 to str2

def editDistance(str1, str2, m, n):
    # If first string is empty, the only option is to insert all characters of the second string into the first
    if m == 0:
        return n

    # If second string is empty, the only option is to remove all characters of the first string
    if n == 0:
        return m

    # If last characters of two strings are same, ignore last characters and get count for remaining strings
    if str1[m - 1] == str2[n - 1]:
        return editDistance(str1, str2, m - 1, n - 1)

    # If last characters are not same, consider all three operations on the last character of first string:
    # 1. Insert
    # 2. Remove
    # 3. Replace
    # Take minimum of these three
    return 1 + min(
        editDistance(str1, str2, m, n - 1),    # Insert
        editDistance(str1, str2, m - 1, n),    # Remove
        editDistance(str1, str2, m - 1, n - 1) # Replace
    )


# Driver code
str1 = "sunday"
str2 = "saturday"

print('Edit Distance is:', editDistance(str1, str2, len(str1), len(str2)))
print("\nPerformed by Joshua Thadi 48")
