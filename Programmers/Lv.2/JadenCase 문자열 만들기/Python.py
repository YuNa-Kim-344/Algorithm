def solution(s):
    answer = ''
    
    s = s.split(" ")
    
    for i in range(len(s)):
        if s[i] != "":
            s[i] = s[i][0].upper() + s[i][1:].lower()
                
    answer = " ".join(s)          

    return answer
