"""
PROBLEM STATEMENT
-----------------

The Triplet Sum
Given an array A[] of N numbers, determine whether or not there exist three elements in A[] whose sum is exactly 0.

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]

Input: nums = []
Output: []

Input: nums = [0]
Output: []

"""
lst = list(map(int, input().split()))
set_lst = set()
lst2 = []

for i in range(0,len(lst)):
    for j in range(i+1,len(lst)):
        for k in range(j+1,len(lst)):
            if lst[i]+lst[j]+lst[k] == 0:
                set_lst.add(tuple(sorted([lst[i],lst[j],lst[k]])))

print(list(set_lst))