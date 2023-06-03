# Ones
# Given a positive integer N,
# N is not divisible by 2 or 5, some multiple of N is a number which in decimal notation is a sequence of 1's.
# Your task is to find the smallest multiple of N


import sys

for N in map(int, sys.stdin):
    dividend = 1
    one = 1
    
    if N == 0:
        print("0")
    else:
        while True:
            if dividend < N:
                dividend = dividend * 10 + 1
                one += 1
            
            k = dividend % N
            if k != 0:
                dividend = k
            else:
                break
        
        print(one)


