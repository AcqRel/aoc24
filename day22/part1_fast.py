from functools import reduce
from operator import xor
import time

def matmul(mat1, mat2):
    return [
        reduce(xor, (c for i, c in enumerate(mat2) if r & (1 << i)))
        for r in mat1
    ]

def matexp(mat, n):
    if n == 1: return mat
    half = matexp(mat, n // 2)
    mat2 = matmul(half, half)
    if n % 2: mat2 = matmul(mat2, mat)
    return mat2

def shift_xor_mat(sh):
    return [(1 << c + sh if 0 <= c + sh < 24 else 0) | 1 << c for c in range(24)]

t1 = time.time()

it1 = matmul(shift_xor_mat(6), shift_xor_mat(-5))
it1 = matmul(it1, shift_xor_mat(11))
it2000 = matexp(it1, 2000)

t = 0
for line in open(0):
    n = int(line)
    t += reduce(xor, (r for i, r in enumerate(it2000) if n & (1 << i)))

t2 = time.time()

print(t)
print(f"Actual time: {t2 - t1:.4}")
