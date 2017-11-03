def laceStrings(s1, s2):
    """
    s1 and s2 are strings.

    Returns a new str with elements of s1 and s2 interlaced,
    beginning with s1. If strings are not of same length, 
    then the extra elements should appear at the end.
    """
    newString = ''
    if s1 == '':
        return s2
    elif s2 == '':
        return s1
    elif len(s1) == len(s2):
        for i in range(len(s1)*2):
            if i%2 == 0:
                newString += s1[i/2]
            else:
                newString += s2[i/2]
        return newString
    elif len(s1) > len(s2):
        for i in range(len(s2)*2):
            if i%2 == 0:
                newString += s1[i/2]
            else:
                newString += s2[i/2]
        newString = newString + s1[len(s2):]
        return newString
    else:
        for i in range(len(s1)*2):
            if i%2 == 0:
                newString += s1[i/2]
            else:
                newString += s2[i/2]
        newString = newString + s2[len(s1):]
        return newString
        
b = laceStrings('abc1234567', 'def')
print (b)