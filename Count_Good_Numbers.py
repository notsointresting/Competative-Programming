# A digit string is good if the digits (0 indexed) at even indices are even
# and the digits at odd indices are prime ( 2,3,5 or 7)

mod = 1000000007

def power(x,y):
    if y == 0:
        return 1

    ans = power(x,y/2)
    ans*= ans
    ans%= mod

    if y%2:
        ans*=x
    ans%= mod
    return ans

n = int(input("Enter Number: "))
odd,even = int(n/2),int(n/2+n%2)
print(power(5,even)*power(4,odd)%mod)
    
