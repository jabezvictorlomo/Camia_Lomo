# Imports the math library
import math

# Asks the user to input sides a and b
side_a=float(input("Enter the side a: "))
side_b=float(input("Enter the side b: "))

# Calculates the square of sides a and b
a = math.pow(side_a,2)
b = math.pow(side_b,2)

# Totals the square of sides a and b
total = a+b

# Completes calculating the hypotenuse by square rooting the total
hypotenuse = math.sqrt(total)

# Shows the final output.
print(f"The hypotenuse is {hypotenuse:.2f}")