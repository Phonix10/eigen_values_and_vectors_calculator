import numpy as np


n = int(input("Enter the size of the square matrix (n x n): "))

print(f"Enter the {n*n} elements row-wise (space-separated):")
elements = list(map(float, input().split()))

if len(elements) != n * n:
    print("Error: Number of elements doesn't match the specified size.")
else:
    A = np.array(elements).reshape(n, n)

    eigenvalues, eigenvectors = np.linalg.eig(A)

    print("\nMatrix A:")
    print(A)

    print("\nEigenvalues:")
    print(eigenvalues)

    print("\nEigenvectors (each column is an eigenvector):")
    print(eigenvectors)
