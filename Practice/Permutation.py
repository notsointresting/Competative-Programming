def swap(a, i, j):
    a[i], a[j] = a[j], a[i]

def permute(a, l, r):
    if l == r:
        print("".join(a))
    else:
        for i in range(l, r+1):
            swap(a, l, i)
            permute(a, l+1, r)
            swap(a, l, i)

if __name__ == "__main__":
    lst = list(map(str,input().split()))
    str_lst = "".join(i for i in lst)
    str = str_lst
    n = len(str)
    permute(list(str), 0, n-1)
