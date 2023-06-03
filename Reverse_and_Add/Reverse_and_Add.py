# Revese and Add
#
# The problem is as follows: choose a number, reverse its digits and add it to the original.
# If the sum is not a palindrome (which means, it is not the same number from left to right and right to left), repeat this procedure.
# For example:
# 195 (initial number) + 591 (reverse of initial number) = 786
# 786 + 687 = 1473
# 1473 + 3741 = 5214
# 5214 + 4125 = 9339 (palindrome)

# In this particular case the palindrome 9339 appeared after the 4th addition.
# This method leads to palindromes in a few step for almost all of the integers.



def reverse(n):
    return int(str(n)[::-1])

def reverse_and_add(n):
    return n + reverse(n)


for i in range(int(input())):
    n = int(input())
    str_n = str(n)
    while n != reverse(n):
        n = reverse_and_add(n)
    print(f'{len(str(n))} {n}')
