import math

# David Jo. Assignment 2 "Higher Order Functions"
# Program prupose: To demonstrate understanding of higher order functions and lambda functions by
# creating a program that takes in a function as an argument and returns the sum of the function operating on numbers
# between the lower and upper bounds (inclusive)

def summation(f, lower, upper):
    """This function accepts arguments that include a function, lower bound,
    and upper bound. It then sums the values from the function for each of
    the numbers between the lower bound and upper bound, inclusive """
    sum_to_return, i  = 0, lower
    while (i <= upper):
        sum_to_return, i = sum_to_return + f(i), i+1
    return sum_to_return

def square(x):
    """ This function calculates and returns the square of the input argument x """
    return x * x

def fourth_power(x):
    """ This function calculates and returns the fourth power of x.
    It uses neither x*x*x*x, x**4, nor math.pow(x, 4) """
    return square(square(x))

def main():
    print("\nUser Input:")
    lower = int(input("Enter a lower bound for the sum: "))
    upper = int(input("Enter an upper bound for the sum: "))

    print("\nProgram Output:")
    print(f"The sum of squares of the numbers from {lower} to {upper} is {summation(square, lower, upper)}")
    print(f"The sum of the fourth powers of the numbers from {lower} to {upper} is {summation(fourth_power, lower, upper)}")
    print(f"The sum of square roots of the numbers from {lower} to {upper} is {summation(lambda x: x**.5, lower, upper)}")


if __name__ == "__main__":
    main()
