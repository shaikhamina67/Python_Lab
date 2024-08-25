#Lab2: Using SciPy Linear Algebra please solve the below problem. Input: 7x + 2y = 8 4x + 5y = 10

import numpy as np
from scipy.linalg import solve

# Coefficient matrix A
A = np.array([[7, 2], [4, 5]])

# Right-hand side vector b
b = np.array([8, 10])

# Solving the linear system
solution = solve(A, b)

# Displaying the solution
print("Solution:")
print(f"x = {solution[0]:.4f}")
print(f"y = {solution[1]:.4f}")

"""Output:
x = 0.7407
y = 1.4074"""
