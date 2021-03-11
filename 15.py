def bernoulli_triangle(n):
    if n == 0:
        return []
    if n == 1:
        return [[1]]
    resultList = [[1]]
    for i in range(1,n):
        tempList = [1]
        for j in range(1,i):
            previousRowPrevioisPosition = resultList[i-1][j-1]
            previousRowSamePosition = resultList[i-1][j]
            tempList.append(previousRowPrevioisPosition + previousRowSamePosition)
        tempList.append(resultList[i-1][i-1] * 2)
        resultList.append(tempList)
    return resultList

print(bernoulli_triangle(5))