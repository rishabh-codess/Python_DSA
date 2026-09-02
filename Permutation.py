def permutation(s1, takenSoFar):
    if (s1 == '') or len(s1)==0:
        print (takenSoFar)
        return 

    ourchar=s1[0]
    smallinput=s1[1:]

    for i in range(0, len(takenSoFar)+1):
        permutation(smallinput, takenSoFar[0:i]+ ourchar+takenSoFar[i:0])

    return 

permutation('c', 'ba')
