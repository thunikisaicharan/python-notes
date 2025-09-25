import array
a = array.array('i',[1,2,3])
b = array.array('i',[4,5,6])
result = array.array('i',[a[i]+b[i] for i in range(len(a))])
print(result)


import numpy as  np
a = np.array([1,2,3])
b = np.array([4,5,6])
result = a+b
print(result)

import numpy as np

arr = np.array([1, 2, 3, 4, 5])
print(arr.ndim)  
print(arr.shape)  
print(arr.size)   
print(arr.dtype)  



import numpy as np

print(np.zeros(5))
print(np.ones(5))
print(np.arange(1, 10, 2))


arr = np.array([10,20,30,40,50])
print(arr[0])
print(arr[-1])
