import heapq

def solution(n, works):
    answer = 0
    
    q = []
    
    if sum(works) <= n:
        return 0
    
    for i in works:
        heapq.heappush(q, -i)
        
    
    while n > 0:
        
        new = heapq.heappop(q) + 1
        heapq.heappush(q, new)
        n -= 1
    
    for j in q:
        answer += j*j
        
    
    return answer
