#Shreeji Patel
#105151171


def palindrome(s):
    if len(s) <= 1 : return True

    if s[0] == s[len(s)-1]:
        return palindrome(s[1:len(s)-1])
    
    else: return False

#print(palindrome('racecar'))
#print(palindrome('python'))
#print(palindrome('madam'))