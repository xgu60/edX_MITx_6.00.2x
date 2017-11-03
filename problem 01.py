s = 'ab'
maxstr = s[0]
index = 0
while index < len(s)-1:
    temp = ''
    temp += s[index]
    for i in range(index+1, len(s)):
        index += 1
        if s[i] >= s[i-1]:
            temp += s[i]  
        else:
            break
    if len(temp) > len(maxstr):
        maxstr = temp
print 'Longest substring in alphabetical order is: ' + str(maxstr)