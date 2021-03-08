def digital_roots(L):
    for i in range(len(L)):
        while L[i] >= 10:
            L[i] = L[i] % 10 + L[i] // 10
    return L
print(digital_roots([98,100,12345,22,0]))