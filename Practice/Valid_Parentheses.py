# Valid Praentheses
valid = ["()","{}","[]",
         "()[]","[]()","(){}","{}()",
         "()[]{}",
         "(){}[]",
         "[](){}",
         "{}()[]",
         "{}[]()",
         "[]{}()",]

string = input()

if string in valid:
    print(True)
else:
    print(False)
