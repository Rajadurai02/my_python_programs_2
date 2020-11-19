import numpy as np
dim_0 = np.array(24)
dim_1 = np.array([1,2,3])
dim_2 = np.array([[1,2,3],[1,2,3]])
dim_3 = np.array([[[1,2,3],[1,2,3]],[[1,2,3],[1,2,3]]])
print(dim_0)
print(dim_1)
print(dim_2)
print(dim_3)

#print dimensions
print(dim_0.ndim)
print(dim_1.ndim)
print(dim_2.ndim)
print(dim_3.ndim)


#creating array with min dim
arr = np.array([1,2,3],ndmin = 5)
print(arr)

print("The dimension of array", arr.ndim)