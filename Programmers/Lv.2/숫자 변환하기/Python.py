from collections import deque

def solution(x, y, n):
    answer = 0
    
    queue = deque([(x, answer)])
    visited = {x}
    
    while queue:
        num , count = queue.popleft()
        
        if num == y:
            return count
        
        for new_num in (num+n, num*2, num*3):
            if new_num <= y and new_num not in visited:
                queue.append((new_num, count + 1))
                visited.add(new_num)
    
    answer = -1
    
        
    return answer
