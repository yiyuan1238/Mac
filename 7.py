def findMax(arr):
    result = arr[0]
    for item in arr:
        if item > result:
            result = item
    return result

def findMaxVersion2(arr):
    result = arr[0]
    for index in range(len(arr)):
        if arr[index] > result:
            result = arr[index]
    return result