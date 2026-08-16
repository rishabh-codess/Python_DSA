def getChar(value):
    if (value==0 or value>26):
        return ""
    return chr(97+value-1)

def ReturnbAllCodes(input):
    if (input==''):
        return['']

    if (len(input)==1):
        singlechar =getChar(int(input))
        return [singlechar]

    
    singleDigit=int(input[0:1])
    DoubleDigit= int(input[0:2])
    mainAns=[]
    ansWithoutFirstDigit= ReturnbAllCodes(input[0:1])
    for eachAns in ansWithoutFirstDigit:
        mainAns.append(getChar(singleDigit)+eachAns)

    if (DoubleDigit>=10 and DoubleDigit<=26):
        ansWithoutDoublDigit= ReturnbAllCodes(input[2:])
        for eachAns in ansWithoutDoublDigit:
            mainAns.append(getChar(DoubleDigit)+eachAns)

    return mainAns

ans = ReturnbAllCodes('1123')
print (ans) 