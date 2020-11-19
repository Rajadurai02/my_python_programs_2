import numpy as np 

arr = np.array([1,2,3,4,5,6,7,8])
print(np.where(arr == 6))

#print indexes of odd numbers
print(np.where(arr%2 != 0))
#print indexes of even numbers
print(np.where(arr%2 == 0))

#search sorted

print(np.searchsorted(arr,4))
print(np.searchsorted(arr,4,side = "right"))
print(np.searchsorted(arr,[4,7,9]))