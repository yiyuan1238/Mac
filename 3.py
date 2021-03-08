def findMax(a,b,c):
    if a > b and a > c:
        return a
    if b > a and b > c:
        return b
    if c > a and c > b:
        return c
    else:
        print('请重新输入')