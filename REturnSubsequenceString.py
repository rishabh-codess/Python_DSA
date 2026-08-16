def sequence(s1, takensofar):

    if (s1 == '')or len(s1)==0:
        print (takensofar)
        return 

    currentchar=s1[0]
    smallinput= s1[1:]

    sequence (smallinput,takensofar+currentchar )
    sequence (smallinput, takensofar)

    return 

s1 = ('abc')
print (sequence (s1, ""))

