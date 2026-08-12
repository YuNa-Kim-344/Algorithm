def solution(dirs):
    answer = 0
    
    dx = [-1, 1, 0, 0] # 좌, 우, 상, 하
    dy = [0, 0, 1, -1]
    
    start = [0, 0]
    visited = set()
    
    for i in dirs:
                   
        if i == "L":
            d = 0
        elif i == "R":
            d = 1
        elif i == "U":
            d = 2
        else:
            d = 3
            
        nx = start[0] + dx[d]
        ny = start[1] + dy[d]
            
        if  nx > 5 or nx < -5 or ny > 5 or ny < -5:
            continue
            
        path = (start[0], start[1], nx, ny)
        b_path = (nx, ny, start[0], start[1])
        if path not in visited:
            visited.add(path)
            visited.add(b_path)
            answer += 1
            
        start[0] = nx
        start[1] = ny
        
    return answer
