from os import system
system("cls")

def clearDigits( s: str) -> str:
    h = ''
    count = 0
    if len(s) == 0:
        return ''
    for i in s:
        if i.isdigit():
            h += ''
            count += 1
        if count == 2:
            return ""
        else:
            h += i
    return h
    
# g = "abc"
g = "cb34"
# g = "a8f"
g = "ag3"
print(clearDigits(g))