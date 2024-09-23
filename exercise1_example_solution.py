"""
Example solution for Exercise 1:
This program demonstrates good coding form, clear and useful commenting, and
how to use conditionals to solve a quadratic equation. Additionally, it introduces
a new concept of using try/except blocks, which may not have been covered in class yet,
but demonstrates how to validate user input and ensure improper input does not
crash your program unexpectedly.

- The program prompts the user to input coefficients for a quadratic equation.
- It checks the validity of the input, calculates the discriminant, and determines
  the nature of the equation's solutions.
- The use of try/except ensures that non-numeric inputs do not cause the program to crash.
"""


def solve_quadratic_equation():
    # Step 1: Prompt user for input values for a, b, and c
    #   Using try/except to catch invalid input:
    #   Try/except blocks allow the program to "try" executing code and "catch" exceptions (errors) that occur.
    #   If an error occurs (e.g., user enters non-numeric values), the program will handle it and continue running, avoiding a crash.
    try:
        a = float(input("Enter the coefficient 'a': "))
        b = float(input("Enter the coefficient 'b': "))
        c = float(input("Enter the constant 'c': "))
    except ValueError:
        print("Invalid input. Please enter numerical values.")
        return

    # Step 1.5: Check if a is zero (not a quadratic equation)
    if a == 0:
        print("The value of 'a' cannot be zero for a quadratic equation.")
        return

    # Step 2: Compute the discriminant
    discriminant = ( b**2 ) - ( 4 * a * c )

    # Step 3: Determine the nature of the solutions based on the discriminant
    if discriminant < 0:
        # No real solutions
        print("There are no real solutions as the discriminant is negative.")
    elif discriminant == 0:
        # One real solution (repeated root)
        x = -b / (2*a)
        print(f"There is one real solution: x = {x}")
    else:
        # Two real solutions
        x1 = (-b + discriminant ** 0.5) / (2*a)
        x2 = (-b - discriminant ** 0.5) / (2*a)
        print(f"There are two real solutions: x1 = {x1}, x2 = {x2}")

# Step 0: Run the quadratic equation solver
solve_quadratic_equation()
