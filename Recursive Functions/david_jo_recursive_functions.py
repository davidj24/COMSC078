# David Jo. Assignment 3 "Recursive Functions"
# Program prupose: To demonstrate understanding of recursion by
# creating a program that uses recursion to display and sum integers from a lower to an upper bound.


def display_em(lower, upper):
    """ This recursive function displays the consecutive integers
    from its lower to its upper bounds """
    # base case
    if lower > upper:
        return

    print(lower)
    display_em(lower+1, upper)

def add_em(lower, upper):
    """ This recursive function calculates the sum of the consecutive
    integers from its lower to its upper bounds"""

    # base case
    if lower > upper:
        return 0

    return lower + add_em(lower+1, upper)

def applyToEach(f, lower_bound, upper_bound):
    """ This higher-order function applies the included function
    to its lower and upper bound arguments"""
    return f(lower_bound, upper_bound)

def main():
    lower = int(input("Enter a lower bound: "))
    upper = int(input("Enter an upper bound: "))
    print("\nThe consecutive integers:")
    applyToEach(display_em, lower, upper)
    print(f"\nAdd up to: {applyToEach(add_em, lower, upper)}")

if __name__ == '__main__':
    main()