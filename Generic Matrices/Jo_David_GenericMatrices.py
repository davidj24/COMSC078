# David Jo. Assignment 7 "Generic Matrices"
# Program prupose: To implement a generic matrix class and its subclasses to practice object oriented programming and inheritance

from fractions import Fraction

class GenericMatrix(object):
    """Abstract class that operates on matrices with the same type of entries"""
    def __init__(self, matrix):
        self.matrix = matrix
        self.num_rows = len(matrix) if matrix else 0
        self.num_cols = len(matrix[0]) if matrix else 0
        print(f"successfully created matrix {matrix} with {self.num_rows} rows and {self.num_cols} columns") if matrix else print("Empty matrix created!")

    def __add__(self, other):
        """Adds two elements of drawn from matrices"""
        pass

    def __mul__ (self, other):
        """For multiplying two elements drawn from matrices"""
        pass

    def __zero__(self):
        """Abstract method for defining the zero element for the type of matrix."""
        pass

    def __addMatrix__(self, other):
        """Adds two matrices with the same types of elements and returns the resulting matrix."""
        if (self.num_cols != other.num_cols) or (self.num_rows != other.num_rows):
            print("Invalid dimensions for addition!")
            return
        
        result = [[self.__zero__() for _ in range(self.num_cols)] for _ in range(self.num_rows)]
        for i in range(self.num_rows):
            for j in range(self.num_cols):
                result[i][j] = self.matrix[i][j] + other.matrix[i][j]
        return result


    def __multiplyMatrix__(self, other):
        """Multiplies two matrices with the same types of elements and returns the resulting matrix."""
        if self.num_cols != other.num_rows:
            print("Invalid dimensions for Multiplication!")
            return

        result = [[sum([self.matrix[i][k] * other.matrix[k][j] for k in range(self.num_cols)]) for j in range(other.num_cols)] for i in range(self.num_rows)]
        return result
        
    def __str__(self):
        """Returns a string representation of the matrix."""
        return '\n'.join([" ".join(str(element) for element in row) for row in self.matrix])



class IntegerMatrix(GenericMatrix):
    """Allows you to add and multiply the elements in an IntegerMatrix"""
    def __init__(self, matrix: list[list[int]]):
        super().__init__(matrix)

    def __add__(self, other):
        """Adds two integer matrices and return the sum"""
        return self.__addMatrix__(other)

    def __mul__(self, other):
        """Multplies two integer matrices and returns the product"""
        return self.__multiplyMatrix__(other)

    def __zero__(self):
        """Returns 0 for as an integer"""
        return 0


class RationalMatrix(GenericMatrix):
    """Allows you to add and multiply the elements in a RationalMatrix"""
    def __init__(self, matrix: list[list[Fraction]]):
        super().__init__(matrix)

    def __add__(self, other):
        """Add and return the sum of two rational numbers"""
        return self.__addMatrix__(other)

    def __mul__(self, other):
        """For multiplying two elements drawn from matrices"""
        return self.__multiplyMatrix__(other)

    def __zero__(self):
        """Returns 0 for as an integer"""
        return Fraction(0, 1)


def main():
    # IntegerMatrix test
    print("Testing IntegerMatrix:")
    m1 = IntegerMatrix([[1, 2, 3],
         [4, 5, 6],
         [1, 1, 1]])
    
    m2 = IntegerMatrix([[1, 1, 1],
         [2, 2, 2],
         [0, 0, 0]])
    
    sum = IntegerMatrix(m1 + m2)
    print(f"The sum is: \n{sum}")

    product = IntegerMatrix(m1 * m2)
    print(f"The product is: \n{product}")


    # RationalMatrix test
    print("\n\nTesting RationalMatrix:")
    m1 = RationalMatrix([[Fraction(1, 5), Fraction(1, 6), Fraction(1, 7)],
         [Fraction(2, 5), Fraction(1, 3), Fraction(2, 7)],
         [Fraction(3, 5), Fraction(1, 2), Fraction(3, 7)]])
    
    m2 = RationalMatrix([[Fraction(1, 6), Fraction(1, 7), Fraction(1, 8)],
         [Fraction(1, 3), Fraction(2, 7), Fraction(1, 4)],
         [Fraction(1, 2), Fraction(3, 7), Fraction(3, 8)]])
    
    sum = RationalMatrix(m1 + m2)
    print(f"The sum is: \n{sum}")

    product = RationalMatrix(m1 * m2)
    print(f"The product is: \n{product}")

    # Test for invalid dimensions
    print("\n\nTesting invalid dimensions for addition and multiplication:")
    m1 = IntegerMatrix([[1, 2, 3],
         [4, 5, 6]])
    
    m2 = IntegerMatrix([[1, 1],
         [2, 2],
         [0, 0],
         [0, 0]])
    
    sum = IntegerMatrix(m1 + m2)
    product = IntegerMatrix(m1 * m2)

if __name__ == "__main__":
    main()