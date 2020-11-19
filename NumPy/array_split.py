import numpy as np 

#spliting one dimensional array
arr = np.array([1,2,3,4,5,6,7,8,9,0])
new_arr = np.array_split((arr),4)
print(new_arr)
for idx,i in np.ndenumerate(new_arr):
    print(idx,i)

#splitting 2d arrays
arr = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15],[16,17,18]])
new_arr = np.array_split(arr,2)
print(new_arr)
new_arr = np.array_split(arr,2,axis = 1)
print(new_arr)
new_arr = np.hsplit(arr,3)
print(new_arr)
new_arr = np.vsplit(arr,3)
print(new_arr)
#it only works on three or more dimension arrays
new_arr = np.dsplit(arr,3)
print(new_arr)