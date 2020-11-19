from numpy import random
#one dimensional array using randint
arr = random.randint(100,size = 5)
print(arr)
#two dimensional array
arr = random.randint(100,size=(4,5))
print(arr)

#one dimensional float array using rand
arr = random.rand(5)
print(arr)
#two dimensional float array
arr = random.rand(4,5)
print(arr)

#using random choices
arr = random.choice([12,34,56,78,23])
print(arr)
#two dimensional array using random choices

arr = random.choice([12,34,56,78,23],(3,4))
print(arr)