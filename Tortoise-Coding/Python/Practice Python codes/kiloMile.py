# converting kilometer into miles
kilometer = float(input("Enter the values in kilometers : "))

# conversion factor
conv_fac = 0.621371

# calculation miles
miles = kilometer * conv_fac
print('%0.2f kilometers is equal to %0.2f miles : ' %(kilometer,miles))

# converting miles into kilometers 
miles_k = float(input("\nEnter the values in miles : "))
kilometer_m = miles_k / conv_fac
print('%0.2f miles is equal to %0.2f kilometer : ' %(miles_k, kilometer_m))

