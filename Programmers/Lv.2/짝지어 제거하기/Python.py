def solution(s):

    while len(s) > 0:
        removed = False
        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                s = s[:i] + s[i+2:]
                removed = True
                break
            
        if len(s) == 0:
            return 1
        if removed == False:
            return 0
            
