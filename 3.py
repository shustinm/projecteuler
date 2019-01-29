#!/bin/python
import math
import time
num = 600851475143

def is_prime(factor):
    if factor % 2 == 0:
        return False
    for j in range(3, int(math.sqrt(factor)) + 1, 2):
        if factor % j == 0:
            return False
    return True

start_time = time.time()
for times, i in enumerate(range(3, int(num/2) + 1, 2)):
    if not num % i:
        if is_prime(num // i):
            print('Found the largest prime factor: {}. Took {} divisions'.format(num // i, times))
            break
end_time = time.time()

print(end_time - start_time, " seconds")
