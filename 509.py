from os import system
system("cls")

def fib(n: int) -> int:
        f = 0
        if n > 1:
            return 0
        j = 1
        while j < n:
            f += (n-1) + (n-2)
            print(f)
            j += 1
        # return f 
n = 3
print(fib(n))