def solution(s):
    answer = True
    
    if s[0] == ')':
        return False
    
    a = 0
    
    for i in range(len(s)):
        if s[i] == '(':
            a += 1
        elif s[i] == ')':
            a+= -1
        
        if a < 0:
            return False
    
    if a != 0:
        return False

    return True
