#copy
import numpy as np 
arr = np.array([1,2,3,4,5])
x = arr.copy()
arr[0] = 12
print(arr)
print(x)

#view
arr1 = np.array([1,2,3,4,5])
xy = arr1.view()
arr1[0] = 12
print(arr1)
print(xy)
#make changes in view
xy[0] = 1
print(xy)

#if check the array own its data using base
ar = np.array([23,45,6,7])
x = ar.copy()
y = ar.view()
print(x.base)
print(y.base)