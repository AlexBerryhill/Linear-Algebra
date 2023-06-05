from sympy import Matrix
import numpy as np

# Define the matrices
matrix1 = Matrix([[0.8, 0, 0], 
                  [0, 1.2, 0], 
                  [0, 0, 1]])
matrix2 = Matrix([[1, 0, -2], 
                  [0, 1, 3], 
                  [0, 0, 1]])

# Multiply the matrices
result = matrix1 * matrix2

# Display the result
print(result)
