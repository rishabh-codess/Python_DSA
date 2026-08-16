def palindromeHelper(s1, start, end):
    if start>end:
        return True
    if (s1[start]!= s1[end]):
        return False
    return palindromeHelper (s1, start+1, end-1)

def palindrome(s1):
    return palindromeHelper (s1, 0, len(s1)-1)

print (palindrome('nitin'))