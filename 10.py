def squareList(arr):
    resultList = []
    for item in arr:
        square = item * item
        resultList.append(square)
    return resultList
print(squareList([1,3,9]))