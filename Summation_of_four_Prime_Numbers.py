# Summation of four Prime Numbers
# APPROACH:
# 1. Find a prime number PN1 such that PN1 < N-7 , preferably p1 is close to n
# 2. if n-PN1 is odd, then PN2 = 3 else PN2 = 2
# Find a pair of primes, PN3 and PN4 that sum to n-PN1-PN2. if PN1 is large then N-PN1-PN2 is small and it will be easy to find PN3 and PN4

import math

def isPrime(n):
    s = int(math.sqrt(n))

    # Traverse from 2 to sqrt(n)

    for i in range(2, s+1):
        # if any divisior found
        # then it is not prime
        if n % i == 0:
            return 0
        
        # if no divisor found
        # then it is prime
        return 1
    
def Num(n):
        # Iterates to check Prime or not
    X = [0]*2
    for i in range(2,(int(n/2)+1)):
            # Call function to check prime
        if isPrime(i)!=0 and isPrime(n-i)!=0:
            X[0] = i
            X[1] = n-i
            return X
        # if two prime numbers are found then return
    
    
    # Function to find four prime numbers
def fourPrime(n):
        # if N <= 7 then 4 numbers are not possible
        
    if n <= 7:
            print("Impossible")
            
        # if it is not even then 2 and 3 are the only possible prime numbers

    if n % 2 != 0:
            # Call the function to get the other two prime numbers 
            # considering first two primes as 2 and 3 
        X = Num(n-5)

        print("2 3", X[0], X[1])
    else:
            # If N is even then 2 and 2 are the only possible prime numbers
        X = Num(n-4)
        print("2 2", X[0], X[1])

fourPrime(int(input("Enter a Number: ")))


        