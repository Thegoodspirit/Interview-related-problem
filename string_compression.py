"""
Given a string in the form 'AAABBBAACCEE' compress it to become 'A3B3A2C2E2' .For this problem you can falsely "compress" 
strings of single or duble letters . For instnce ,it is okay for 'AAB' of return 'A2B1' even though this tehiinically take ore 
space.

The function should also be a case sensitive 'AAAaaa' retuns 'A3a3'
"""


def compress(s):

    r = ""
    l = len(s)

    if l == 0:
        return ""
    
    if l == 1:
        return s+"1"

    last = s[-1]
    cnt = 1
    i = 1

    while i < l:

        if s[i] == s[i-1]:
            cnt += 1
        else:
            r = r + s[i-1] + str(cnt)
            cnt = 1
      
        i += 1

    r = r + last + str(cnt)
    
    return r

print(compress("AAaabbCcB"))