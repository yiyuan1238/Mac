def add(a,b):
    return a+b

m = add(add(1+2)+3) #方法一
print(m)

n = add(1,2) #方法二
m = add(n,3)
print(m)
