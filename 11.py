def f(a):
    b = 0
    for i in range(len(a)):
        if i % 2 == 0:
            b = b + a[i]
    return b

print(f([1,2,3,4,5]))