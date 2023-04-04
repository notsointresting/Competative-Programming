# Find First and Last Position of Elment in Sorted Array

arr = list(map(int,input().split()))
Target = int(input())
lst = []
for i in range(len(arr)):
    if arr[i] == Target:
        lst.append(i)        

if Target in arr:
    print(lst)
else:
    print('[-1,-1]')
    
