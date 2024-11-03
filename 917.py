from os import system
system("cls")

def reverseOnlyLetters(s: str) -> str:
    h = ''
    h1 = ''
    for i in s.split("-"):
        h += i
    for i in s.split("-"):
        h1 += "-"

    return h 
x = "ab-cd"
print(reverseOnlyLetters(x))
