# Search a 2D Matrix

lst = []
Flag = False
n = int(input("Enter Number of Rows---> "))
Target = int(input("Enter Target Number---> "))

for i in range(n):
    lst.append(list(map(int,input().split())))

for i in lst:
    for j in i:
        if j == Target:
            Flag = True
            break

if len(lst[0]) == 0:
    print('[-1][-1]')
elif Flag:
    print(Flag)
else:
    print(False)
    

