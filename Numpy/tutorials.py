# pip install numpy
# import numpy
import numpy as np

# create nth dimension array
_1d = [8, 7, 6]
_1dnew = np.array(_1d, dtype=int)
print(_1dnew)

_2d = [[1, 2, 3], [4, 5, 6]]
_2dnew = np.array(_2d, dtype=int)
print(_2dnew)

_3d = [[11, 22, 13], [14, 5, 16]]
_3dnew = np.array(_3d, dtype=int)
print(_3dnew)

# Arithmetical Operations

print("subtract: ", np.subtract(_3dnew, _2dnew))
print("add: ", np.add(_3dnew, _2dnew))
print("multiply: ", np.multiply(_3dnew, _2dnew))
# print("divide: ", np.divide(_3dnew, _2dnew))

# comparison
print(_2dnew > 4)

# shape of array n x n, length
print(_2dnew.shape, len(_2dnew)) # 

