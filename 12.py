def factor(n):
    result = []
    i = 1
    while i <= n:
        if n % i == 0:
            result.append(i)
        i += 1
    return result
print(factor(12))