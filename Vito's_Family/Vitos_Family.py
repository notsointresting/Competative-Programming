# Vito's Family
# Vito wants to minimize total distance to all of his relatives.

# Input
# The first line contains the number of test cases T.
# You will be given te integer number of relatives r
# And The street numbers s
# Several relatives can live on the same street number.

# Input:
# 2 ---> Testcase
# 2 2 4---> R
# 2 4
T = int(input())
for i in range(T):
    s = list(map(int,input().split()))
    r = s[0]

    s.sort()
    
    mid = s[r//2]
    ans = 0
    for j in range(1,r+1):
        ans += abs(s[j]-mid)
    print(ans)


