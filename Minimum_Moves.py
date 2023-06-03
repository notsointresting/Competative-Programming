def minMoves2(nums):
    nums.sort()  # Sort the array in ascending order
    median = nums[len(nums) // 2]  # Find the median element
    
    moves = 0
    for num in nums:
        moves += abs(num - median)  # Calculate the absolute difference from the median
    
    return moves

nums = list(map(int,input().split()))
result = minMoves2(nums)
print("Minimum number of moves:", result)
