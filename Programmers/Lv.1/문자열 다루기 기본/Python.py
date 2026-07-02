def solution(s):
    answer = True
    
    if len(s) != 4 and len(s) != 6:
        return False
    
    for i in range(len(s)):
        if s[i] < '0' or s[i] > '9' :
            return False
    
    return answer
