import numpy as np 
arr = np.array([[[1,2,3],[1,2,3]],[[1,2,3],[1,2,3]]])

#using nditer
for x in np.nditer(arr):
    print(x)

#iterating array with different data types
a = np.array([1,1,0])
for x in np.nditer(a, flags = ['buffered'], op_dtypes = ['S']):
    print(x)

#iterating differnt step size
ar = np.array([[1,2,3],[4,5,6]])
for x in np.nditer(ar[:,::2]):
    print(x) 

#using ndenumerate
for idx,x in np.ndenumerate(arr):
    print(idx, x)