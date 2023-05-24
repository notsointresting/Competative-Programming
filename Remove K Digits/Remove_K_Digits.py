Num,K = map(str,input("Enter Number and K value---> ").split())

stack = []
K = int(K)

for i in Num:
    while K > 0 and stack and stack [-1] > i:
        K-=1
        stack.pop()
    stack.append(i)

#stack = stack[:len(stack)-K]
print(*stack)

