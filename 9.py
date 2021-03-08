def ifContains(arr,target):
    for item in arr:
        if item == target:
            return True
    return False

def findCommon(a,b):
    result = []
    for i in a:
        for j in b:
            if i == j and not ifContains(result,i):
                result.append(i)
    return result
print(findCommon([1,1,2,3],[0,1,2]))