import numpy as np
from sympy import Matrix
from sympy import sqrt
# L = [
#     [ 2,-1,-1,0,0],
#     [-1,3,-1,0,-1],
#     [-1,-1,3,-1,0],
#     [ 0,0,-1,2,-1],
#     [ 0,-1,0,-1,2]
# ]
L = [
    [4,-1,0,0,0,0,-1,-1,-1],
    [-1,3,-1,0,0,0,0,-1,0],
    [0,-1,3,-1,0,0,-1,0,0],
    [0,0,-1,3,-1,0,0,-1,0],
    [0,0,0,-1,3,-1,-1,0,0],
    [0,0,0,0,-1,3,0,-1,-1],
    [-1,0,-1,0,-1,0,4,0,-1],
    [-1,-1,0,-1,0,-1,0,4,0],
    [-1,0,0,0,0,-1,-1,0,3]
]
M = Matrix(L)
eigenvalues_sympy = M.eigenvals()
actual_eigenvalues = list(eigenvalues_sympy.keys())
# print(eigenvalues_sympy)
# zero = actual_eigenvalues[0].evalf()
# one = actual_eigenvalues[1].evalf()
# two = actual_eigenvalues[2].evalf()
# three = actual_eigenvalues[3].evalf()
# print((zero))
eigenvalues_numpy = np.linalg.eigvals(L)
print(eigenvalues_numpy.round(3))
one = eigenvalues_numpy[1]
two = eigenvalues_numpy[2]
three = eigenvalues_numpy[3]
four = eigenvalues_numpy[4]
five = eigenvalues_numpy[5]
six = eigenvalues_numpy[6]
seven = eigenvalues_numpy[7]
eight = eigenvalues_numpy[8]
# print((one*two*three*four*five*six*seven*eight)/9)

x=0
for i in range(2,6):
    x=x+i
    print(x)
