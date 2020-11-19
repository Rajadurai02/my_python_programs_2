import numpy as np 

#one dimensional slicing
#syntax array_name[start:end:step]
arr = np.array([1,2,3,4,5,6,7])
print(arr[1:4])
print(arr[:5])
print(arr[3:])
print(arr[1:6:2])
print(arr[-5:-2])
print(arr[::2])
print(arr[::-1])

#two dimensional array
ar = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(ar[0, 2:4])
print(ar[0:2, 1])
print(ar[1:3, 2:4])