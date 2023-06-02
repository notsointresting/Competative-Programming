# Return the maximum value of length(word[i]) Multiply with length(word[j])
# Where the Two words do not share common letters
# if no such two words exist, return 0

#lst = map(str,input("Enter word list---> ").split())


lst_alpha = [chr(i) for i in range(65,91)]
print(lst_alpha)

String_alpha = "".join(i for i in lst_alpha).lower()
print(String_alpha)
