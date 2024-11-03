from os import system
system("cls")


def sortArrayByParity(nums: list):
    ls = []
    ls1 = []
    for i in nums:
        if i % 2 == 0:
            ls.append(i)
        else:
            ls1.append(i)
    n = ls + ls1
    
    return n


n = [3,1,2,4]
print(sortArrayByParity(n))