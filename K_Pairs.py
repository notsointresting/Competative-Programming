def findPairs(nums, k):
    count = 0
    numFreq = {}

    for num in nums:
        if k == 0:
            if numFreq.get(num, 0) >= 1 and numFreq.get(num, 0) < 2:
                count += 1
                numFreq[num] = numFreq.get(num, 0) + 1
        else:
            if num + k in numFreq:
                count += 1
        
        numFreq[num] = numFreq.get(num, 0) + 1

    return count

nums = [3, 1, 4, 1, 5]
k = 2
result = findPairs(nums, k)
print("Number of unique k-diff pairs:", result)
