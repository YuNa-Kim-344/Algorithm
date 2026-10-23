def solution(routes):
    answer = 0
    
    routes.sort(key = lambda x : x[1])
    
    c = routes[0][1]
    answer += 1
    
    for start, end in routes[1:]:
        if c < start :
            answer += 1
            c = end
    
    
    return answer
