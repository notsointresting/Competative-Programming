# Hartal ---> Strike
# each party declares a number of hartals h 
# that denotes the average number of days between two successive hartals declared by the party.
# we always start the simulation on a sunday. 
# There is no hartals on either Fridays or Saturdays.

def hartals(n, p, h):
    days = [0] * n 
    for i in range(len(p)):
        for j in range(p[i]-1, n, h[i]):
            if j % 7 != 5 and j % 7 != 6:
                days[j] = 1
    return sum(days)


t = int(input())
for i in range(t):
    n = int(input())
    p = []
    h = []
    for j in range(int(input())):
        p.append(int(input()))
        h.append(p[-1])
    print(hartals(n, p, h))

