def solution(n, stations, w):
    answer = 0
    
    used = []
    
    for i in stations:
        left = max(i-w, 1)
        right = min(i+w, n)
        used.append((left, right))
    
    print(used)
    
    used.sort()
    not_used = []
    one_W = 2*w+1 # 한 기지국 당 범위
    l = 1
    
    for start, end in used:
        if l < start:
            not_used.append((l, start-1))
            
        l = end+1
        
    if l <= n:
        not_used.append((l, n))
    
    for s, e in not_used:
        n_u = e-s+1
        answer += (n_u+one_W -1)//one_W

    return answer
