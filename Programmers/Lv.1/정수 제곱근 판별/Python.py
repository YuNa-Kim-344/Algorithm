import math

def solution(n):
    answer = 0
    
    sqrt = int(math.sqrt(n))
    
    if sqrt * sqrt == n:
        answer = (sqrt+1) * (sqrt+1)
    else:
        answer = -1
    
    return answer
