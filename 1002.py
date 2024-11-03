from os  import system
system("cls")
#ishlanmadi ex g'oya bor lekin yoza olmayabman 
def commonChars(words: list):
    h = []
    for i in range(len(words)):
        if words[i][i] in words[i]:
            print(words)
n = ["bella","label","roller"]
print(commonChars(n))