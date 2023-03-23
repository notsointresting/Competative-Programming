while True:
    # N - Number of lines, M - Number of Columns
    N,M = map(int,input("Enter N and M---> ").split())
    if N == 0 and M == 0:
        break
    
    lst = []

    # Getting input from user as string and storing it into list.
    for _ in range(N):
        lst.append(input().strip())



    for i in range(N):
        for j in range(M):
            # Check if the cell is a safe cell ( means not mine *)
            if lst[i][j] == '.':
                # Initialize a counter to count the number of adjacent mines
                cnt = 0

                # i-1 to i+2 means previous row, current row and current row+1
                for r in range(i-1,i+2):
                    # j-1 to j+2 means previous col of previous row, current col of current row and current col +1 of current col +1
                    for c in range(j-1,j+2):
                        # If the adjacent cell is a mine, increment the counter
                        if r in range(0,N) and c in range(0,M) and lst[r][c] == '*':
                            cnt+=1
                # Update the current cell with the count of adjacent mines
                lst[i] = lst[i][:j] + str(cnt) + lst[i][j+1:]
    print()
    for r in lst:
        print(r)
            
