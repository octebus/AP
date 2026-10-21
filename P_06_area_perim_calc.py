# Ask the user for the width and height
# (assume they put in valid data)
width = float(input("Please enter your width: "))
height = float(input("Please enter your height: "))

# Calculate the area / perimeter
area = width * height
perimeter = 2 * (width + height)

# Output the area and perimeter

print(f"\nThe area is {area} units.")
print(f"\nThe perimeter is {perimeter} units.")