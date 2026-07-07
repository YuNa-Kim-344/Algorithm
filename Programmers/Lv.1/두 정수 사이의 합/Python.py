def solution(a, b):
    answer = 0
    
    if a > b:
        t = b
        b = a
        a = t
        
    for i in range(a, b+1):
        answer += i
    
    return answer
