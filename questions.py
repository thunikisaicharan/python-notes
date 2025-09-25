a = int(input("enter first number"))
b = int(input("enter second number"))
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)



a = 6
b = 5

a = a+b
b = a-b
a = a-b

print("after swapping:")
print("a =", a)
print("b =", b)


a = int(input("enter first number: "))
b = int(input("enter second number: "))

if a == b:
    print("the number are equal.")
else:
    print("the number are not equal.")


import array
nums = array.array('i',[1,2,3,4,5])
print(nums[::-1])


import array
nums = array.array('i',[1,2,3])
total = sum(nums)
average = total/len(nums)
print(sum(nums))
print(average)


import numpy as np

arr = np.array([1,2,3,4,5,6])
reshaped_arr = arr.reshaped((2,3))import numpy as np

a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])
result = np.dot(a, b)

print(result)
 
print("reshaped array: ",reshaped_arr)


import numpy as np

a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])
result = np.dot(a, b)

print(result)
