def solution(n):
    answer = 0
    
    a, b = 0, 1
    
    for _ in range(2, n+1):
        a, b = b, a+b
        
    answer = b % 1234567
    
    return answer
