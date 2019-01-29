#!/bin/python
a, b = 1, 2
sum_even = b
while b <= 4000000:
    a, b = b, b + a
    if b % 2 == 0:
        sum_even += b
    else:
        pass
print(sum_even)
