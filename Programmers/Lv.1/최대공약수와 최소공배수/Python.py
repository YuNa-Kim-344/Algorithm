def solution(n, m):
    answer = []
    
    a = n*m
    
    while n != m:
        if n < m:
            m -= n
        else:
            n -= m

    answer.append(n) 
    answer.append(a//n)
    
    return answer
