# There are N friends are playing a game
# And they are numbered as  1 to N
# They are sitted in circular so nth next person is 1st and 1st next person is 2nd

while True:
    N,k = map(int,input("Enter Values for N and K---> ").split())

    lst = [ i for i in range(1,N+1)]

    def GetIndex(curIndx, k, size):
        nw_indx = curIndx + k - 1
        if nw_indx >= size:
            nw_indx %= size
        return nw_indx

    def GetAns(lst,indx):
        size = len(lst)
        if size == 1:
            return lst[0]
        else:
            lst.pop(indx)
            return GetAns(lst,GetIndex(indx,k,size-1))
    print(GetAns(lst,GetIndex(0,k,N)))


        
    
