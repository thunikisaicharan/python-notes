import array
floats = array.array('f',[1.1,2.2,3.3])
print(floats)

import array
nums = array.array('i',[10,20,30,40])
print(nums[0])
print(nums[1])
print(nums[2])
print(nums[-1])


import array
nums = array.array('i',[10,20,30,40,50])
print(nums[1:4])
print(nums[::-1])


import array
nums = array.array('i',[1,2,3])
nums.append(4)
print(nums)


nums.insert(1,10)
print(nums)


nums.remove(10)
print(nums)


del nums[0]
print(nums)


import array
nums = array.array('i',[10,20,30,40,50])
print("first element:",nums[0])
print("second element:",nums[-1])

import array
nums = array.array('i',[10,20,30,40,50])
print(nums[2:5])


import array
nums = array.array('i',[10,20,30,40,50])
print(nums[-4:-1])


import array
nums = array.array('i',[10,20,30,40,50])
print(nums[::2])


import array
arr = array.array('i',[5,10,15,20,25,30])
#slice first 4 element
slice_arr = arr[:4]
#calculate sum using a loop
total = 0
for num in slice_arr:
    total+=num
    print("sliced array:",slice_arr)
    print("sum",total)


import array
nums = array.array('i',[10,20,30,40,50])
print(nums[::-1])









