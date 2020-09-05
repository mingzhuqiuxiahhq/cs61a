def paths(m, n):
    if m <= 1 or n <= 1:
        return 1
    else:
        return paths(m-1, n) + paths(m, n-1)

def knapsack(n,k):
    if n == 0:
        return k == 0
    with_last = knapsack(n // 10, k- (n%10))
    without_last = knapsack(n // 10, k)
    return with_last or without_last

def partit(n,m):
    if n <= 1:
        return 1
    elif n < 0 :
        return 0
    elif m == 0:
        return 0
    else:
        return partit(n-m,m) + partit(n,m-1)

def remove(n, digit):
    kept, digits = 0, 0
    while n > 10:
        n, last = n//10, n%10
        if last != digit:
            kept = kept + last *10 **digits
            digits = digits + 1
    return kept
