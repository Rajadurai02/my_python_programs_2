from numpy import random
import numpy as np 
arr = np.array([12,34,56,78,9,0])
random.shuffle(arr)
print(arr)

print(random.permutation(arr))