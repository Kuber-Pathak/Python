import numpy as np
#some basic funtions
a = np.array([1,2,3]);
print("The array a is:",a)

# get type
print("The data type of a is:",a.dtype)

#get size
print("The item size of a is:",a.itemsize)

#get total bytes
print("The total byte used bt a is",a.nbytes)

# get diminsion
print(f"The dimension of a is:{a.ndim}\n")

b = np.array([[1,2,3],[4,5,6]])
print("The array b is:",b)

# get shape
print(f"The shape of b is:{b.shape}\n")

