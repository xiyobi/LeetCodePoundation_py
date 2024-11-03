from os import system
system("cls")

def distributeCandies(candyType:list) -> int:
    n = int(len(candyType)/2)
    s = len(set(candyType))
    return min(s,n)
n = [1,1,2,2,3,3]
print(distributeCandies(n))