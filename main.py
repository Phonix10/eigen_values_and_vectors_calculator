import numpy as np

# Step 1: Get matrix size
n = int(input("Enter the size of the square matrix (n x n): "))

# Step 2: Input matrix elements
print(f"Enter the {n*n} elements row-wise (space-separated):")
elements = list(map(float, input().split()))

# Step 3: Convert list to matrix
if len(elements) != n * n:
    print("Error: Number of elements doesn't match the specified size.")
else:
    A = np.array(elements).reshape(n, n)

    # Step 4: Calculate eigenvalues and eigenvectors
    eigenvalues, eigenvectors = np.linalg.eig(A)

    # Step 5: Display results
    print("\nMatrix A:")
    print(A)

    print("\nEigenvalues:")
    print(eigenvalues)

    print("\nEigenvectors (each column is an eigenvector):")
    print(eigenvectors)
