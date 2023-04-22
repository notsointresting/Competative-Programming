# Jolly the Jumper

N = int(input("Enter length of list---> "))
List = list(map(int,input().split()))
lst = []
lst2 = []

for i in range(0,len(List)-1):
    lst.append(abs(List[i]-List[i+1]))

for i in range(1,N):
    lst2.append(i)


lst.sort()
if lst==lst2:
    print("Jolly")
else:
    print("Not Jolly")
