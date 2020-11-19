import numpy as np 
a = np.array([1,2,3,4,5])
ar = np.array([[1,2,3,4,5],[1,2,3,4,5]])
arr = np.array([[[1,2,3,4,5],[1,2,3,4,5]],[[1,2,3,4,5],[1,2,3,4,5]]])

#iterating a one dimension array
for x in a:
    print(x)

#iterating two dimension array
for x in ar:
    print(x)

#printing every single array element in two dimensional array
for x in ar:
    for y in x:
        print(y)

#iterating three dimensional array
for x in arr:
    print(x)

#printing every single array element in three dimensional array
for x in arr:
    for y in x:
        for z in y:
            print(z)