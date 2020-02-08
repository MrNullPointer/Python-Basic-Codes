import time         #importing time library to calculate the execution time
import numpy as np  #importing the numpy library

#time before multiplication is done
tick = time.time() * 1000

#creating a first 2x2 matrix a:
a = np.random.rand(2,2)

#generating another 2x2 matrix b:
b = np.random.rand(2,2)

#dot product of matrix a and b is stored in matrix c:

c = np.dot(a,b)

#time after the multiplication is done
tock = time.time()*1000

#printing Values
print("The first matrix is:",a)
print("The second matrix is:",b)
print("The final matrix after the dot product of a and b is:",c)
print("The execution time of this entire code is:", tock-tick, "ms")