import numpy as np
#one dimension array indexing
arr_1 = np.array([1,2,3,4,5])
print("The second element of array:",arr_1[1])
print("The fivth element of array:",arr_1[4])

#two dimensional
arr_2 = np.array([[1,2,3],[4,5,6]])
print("The second element of first array:",arr_2[0,1])
print("The fivth element of second array:",arr_2[1,2])

#three dimensional
arr_3 = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print(arr_3[0,1,2])
print(arr_3[1,0,1])

#negative indexing
#negative represents backwards
print("from negative indexing:",arr_1[-1])
print(arr_1[-3])

#one dimensional array maths
print(arr_1[1] + arr_1[3])
print(arr_1)
print(arr_1[1] - arr_1[3])
print(arr_1[1] * arr_1[3])
print(arr_1[1] / arr_1[3])