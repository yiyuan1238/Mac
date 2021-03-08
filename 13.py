def replaceFn(foo):
    charList = []
    for char in foo:
        charList.append(char)
    for i in range(len(charList)):
        if i != 2 and charList[i] == charList[2]:
            charList[i] = '#'

    resultStr = ''
    for char in charList:
        resultStr += char
    return resultStr
print(replaceFn('bubble'))