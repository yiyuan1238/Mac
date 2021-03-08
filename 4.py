def accumulateSum(n):
    if n == 0:
        return 0
    return n + accumulateSum(n - 1)
print(accumulateSum(5))