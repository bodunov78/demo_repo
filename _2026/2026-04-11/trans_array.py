import numpy as np

matrix = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
])

columns = matrix[:, 1:3]
print(type(matrix))
# a=[[1,2,3],[4,5,6],[7,8,9]]
#
#
# c=a[:,1]
# print(a[:,1])