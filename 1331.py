from os import system
system("cls")

def arrayRankTransform(arr:list):
    temp = arr
    g = []
    for j in temp:
        g.append(j)
    c = []
    arr.sort()
    for i in g:
        n = arr.index(i)
        c.append(n+1)

    return c

arr = [100,100,100]
# arr = [40,10,20,30]

print(arrayRankTransform(arr))