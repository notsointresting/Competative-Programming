# Euclid, it is known that for any two positive integers a and b, there exist 
# such integers X and Y that AX + BY = D, where D is the greatest common divisor of a and b.
# The problem is to find the coressponding X,Y and D for a given A and B.


def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)

def extended_gcd(a,b):
    if b==0:
        return a,1,0
    else:
        d,x,y = extended_gcd(b,a%b)
        return d,y,x-(a//b)*y

a,b = map(int,input("Enter two numbers---> ").split())

print(sorted(extended_gcd(a,b)))
