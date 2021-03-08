def Sumevenposition(list):
    result = 0
    for i in range(len(list)):
        if i % 2 == 0:
            result = result + list[i]
    return result
print(Sumevenposition([1,2,3,4,5,6,7,8,9]))