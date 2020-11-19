import numpy as np 

#joining ine dimensional array
arr1 = np.array([1,2,3,4])
arr2 = np.array([5,6,7,8])
arr = np.concatenate((arr1,arr2))
print(arr)

#joining two dimwnsional array
arr1 = np.array([[1,23,4],[1,234,5]])
arr2 = np.array([[1,23,4],[1,234,5]])
arr = np.concatenate((arr1,arr2),axis =1)
print(arr)

#joining three dimensional array
arr1 = np.array([[[1,2,3],[1,2,3]],[[1,2,3],[1,2,3]]])
arr2 = np.array([[[1,2,3],[1,2,3]],[[1,2,3],[1,2,3]]])
arr = np.concatenate((arr1,arr2),axis=2)
print(arr)

#using stack
arr1 = np.array([1,2,3,4,5])
arr2 = np.array([6,7,8,9,0])
arr = np.stack((arr1,arr2),axis = 1)
print(arr)

#usig vertical stack
arrv = np.vstack((arr1,arr2))
print(arrv)
#using horizontal stack
arrh = np.hstack((arr1,arr2))
print(arrh)
#using dstack
arrd = np.dstack((arr1,arr2))
print(arrd)