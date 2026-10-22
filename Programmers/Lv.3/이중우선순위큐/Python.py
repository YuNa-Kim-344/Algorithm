import heapq

def solution(operations):
    answer = []
    
    for i in range(len(operations)):
        operations[i] = operations[i].split(" ")
        
    q = []
    
    for a, b in operations:
        b = int(b)
        if a == "I":
            heapq.heappush(q, b)
        else:
            if not q:
                continue
                
            if b == -1:
                heapq.heappop(q)
            else:
                q.remove(max(q))
                heapq.heapify(q)
                
    if not q:
        answer = [0, 0]
    else:
        answer = [max(q), q[0]]
    
    return answer
