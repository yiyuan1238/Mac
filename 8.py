def Commonnumber(list1,list2):
    result = []
    for i in list1:
        for j in list2:
            if i == j:
                result.append(i)
    return result
print(Commonnumber([1,2,3],[0,1,2]))