# The factorial function, n! is defined as follows:
# 0! = 1
# n! = n * (n-1)! for n > 0

# we say that a divides b if there exists an integer k such that
# a * k = b

import math

while True:
    
    n, m = map(int, input().split())
        
    fact = math.factorial(n)
        
    if fact % m == 0:
        print(m, "divides", n, "!")
    else:
        print(m, "does not divide", n, "!")
    
    








