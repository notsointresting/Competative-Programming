def is_prefix(word, s):
    if len(word) > len(s):
        return False
    for i in range(len(word)):
        if word[i] != s[i]:
            return False
    return True

def count_prefixes(words, s):
    count = 0
    for word in words:
        if is_prefix(word, s):
            count += 1
    return count

n = int(input("Enter the number of words: "))
words = []
print("Enter the words:")
for _ in range(n):
    words.append(input())

s = input("Enter the string: ")
count = count_prefixes(words, s)
print(f"Number of prefixes of '{s}' in the word list: {count}")
