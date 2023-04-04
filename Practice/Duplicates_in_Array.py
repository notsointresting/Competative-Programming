# Find all Duplicates in an Array

lst = list(map(int,input().split()))
lst2 = []
occurance =  set(tuple(tuple(f"{i}:{lst.count(i)}".split(':')) for i in lst))



for i in occurance:
    if i[1] == '2':
        lst2.append(i[0])
print(lst2)

