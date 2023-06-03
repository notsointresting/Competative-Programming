# Primary Arithmetic
# Children are taught to add multi-digit numbers from right-to-left one digit at a time.
# Many find the "carry" operation - in which a 1 is carried from one digit position to be added to the next - to be a significant challenge.
# Your job is to count the number of carry operations for each of a set of addition problems so that educators may assess their difficulty.

# Sample Input 1	Sample Output 1
# 123 456         No carry operation.
# 555 555         3 carry operations.
# 123 594         1 carry operation.



while True:
    a,b = map(int,input("Enter two numbers---> ").split())
    if a==0 and b==0:
        break
    else:
        carry = 0

    while a>0 or b>0:
        if a%10 + b%10 >= 10:
            carry += 1

        a //= 10
        b //= 10


    if carry == 0:

        print("No carry operation.")
    elif carry == 1:
        print("1 carry operation.")
    else:
        print(carry,"carry operations.")


