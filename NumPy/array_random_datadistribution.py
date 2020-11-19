#Data Distribution is a list of all possible values, and how often each value occurs
from numpy import random
#one dimensional
arr = random.choice([1,2,3,4],p=[0.2,0.2,0.6,0.0],size = 100)
print(arr)
#two dimensional array
arr = random.choice([23,24,25,26],p=[0.8,0.1,0.1,0.0],size=(4,4))
print(arr)