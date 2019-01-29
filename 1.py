#!/bin/python
num = 1000
#print(sum(range(3, num + 1, 3)) + sum(range(5, num + 1, 15)) + sum(range(10, num + 1, 15)))
nums = list(range(3, num, 3)) + list(range(5, num, 15)) + list(range(10, num, 15))
print(sum(nums))
