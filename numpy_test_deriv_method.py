import numpy as np

arr_ = np.polynomial.Polynomial(np.array([2,4,6,8,10,12,14,16,18,20])[::-1])

print(arr_)

dx = arr_.deriv()

print(dx)

dx_4 = dx(4)
dx_5 = dx(5)

print(dx_4, dx_5)