#!/bin/python

def check_palindrome(num):
    str_num = str(num)
    for i in range(len(str_num) // 2):
        if not str_num[i] == str_num[-i - 1]:
            return False
    return True

for i in range(999, 99, -1):
    for j in range(i, 1000):
        delta = j - i
        check_num = (i + delta) * (i - delta)
        if check_palindrome(check_num):
            print("{} * {} = {}".format(i + delta, i - delta, check_num))
            exit()
        
