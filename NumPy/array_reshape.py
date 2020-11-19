import numpy as np 
arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
#convert  to two dimensional
new_arr = arr.reshape(3,4)
print(new_arr)
#convert to three dimensional
new_arrr = arr.reshape(2,2,3)
print(new_arrr)
print(new_arrr.base)

#convert to 1d array
new = new_arr.reshape(-1)
print(new)
