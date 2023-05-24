S = input("Enter IP ADDRESS---> ")
lst =[]


def backtrack(i, dots, curIP):
    if dots == 4 and i == len(S): # Remove last char "."
        print(curIP)
        lst.append(curIP[:-1])

    for j in range(i,min(i+3,len(S))):
        if int(S[i:j+1]) < 256 and (i == j or S[i] != "0"):
            backtrack(j+1,dots + 1,curIP+S[i:j+1] + ".")

            
backtrack(0,0,"")
print(lst)


