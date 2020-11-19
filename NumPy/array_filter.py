import numpy as np 
arr = np.array([12,34,56,78,9])
x = [True,False,True,False,True]
new_arr = arr[x]
print(new_arr)

#filtering based on condition
x = []
for i in arr:
    if i % 2 == 0:
        x.append(True)
    else:
        x.append(False)
new_arr = arr[x]
print(new_arr)

#in one line

x = arr % 2 == 0
new_arr = arr[x]
print(new_arr)