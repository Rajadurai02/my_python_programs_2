import numpy as np 
arr = np.array([1,2,3,4])
ar = np.array([[1,2,3],[4,5,6]])
a = np.array([[[1,2,3],[4,5,6]],[[1,2,3],[3,4,5]]])
print("shape of arr array is:",arr.shape)
print("shape of ar array is:",ar.shape)
print("shape of a array is:",a.shape)


#dimension 5
dim5 = np.array([1,2,3,4],ndmin = 5)
print("shape ao array is:",dim5.shape)
