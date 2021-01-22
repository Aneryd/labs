import numpy as np
import random

def matrixmult (A, B):
    rows_A = len(A)
    cols_A = len(A[0])
    rows_B = len(B)
    cols_B = len(B[0])

    if cols_A != rows_B:
      print("Cannot multiply the two matrices. Incorrect dimensions.")
      return

    C = [[0 for row in range(cols_B)] for col in range(rows_A)]
    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                C[i][j] += A[i][k] * B[k][j]
    return C


count = 4
for i in range(9):
    matrix1 = [[random.randint(0,10) for i in range(count)] for j in range(count)]
    matrix2 = [[random.randint(0,10) for k in range(count)] for l in range(count)]
    count += 1
    print(matrixmult(matrix1, matrix2))