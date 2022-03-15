def recursion(n):
    if n == 1:
        return 1
    else:
        return n * recursion(n-1) #factorial

print(recursion(5))

def add(k):
    if k == 1:
        return 1
    else:
        return k + add(k-1)
print(add(5))
