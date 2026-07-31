from collections import deque

def solution(priorities, location):
    answer = 0
    
    process = deque()
    
    for i in range(len(priorities)):
        process.append((i, priorities[i]))
        
    while process:
        point = process.popleft()
        
        higher = False
        
        for p in process:
            if point[1] < p[1]:
                higher = True
                break
        
        if higher:
            process.append(point)
        else:
            answer += 1

            if point[0] == location:
                return answer
        
    return answer
