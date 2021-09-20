# Team Members: Callie Walker
# Course: CS151 DR. Rajeev
# Date: 9/22/21
# Programming Assignment: 1
# Program Inputs: The dimensions - width, length, height
# Program Outputs: Total area to be painted (minus floor), amount primer and paint needed

width = input("Enter the width: ")
length = input("Enter the length: ")
height = input("Enter the height: ")

width_int = int(width)
length_int = int(length)
height_int = int(height)

area = (width_int * length_int * height_int) * 5

primer = area / 200
paint = area / 350

print("The total area is: ", area, "feet \n", "Gallons of primer needed: ", primer, "\n", "Gallons of paint needed: ", paint)


