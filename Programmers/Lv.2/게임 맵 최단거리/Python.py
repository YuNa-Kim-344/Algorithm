from collections import deque

def solution(maps):
    answer = -1
    
    row = len(maps)
    col = len(maps[0])
    
    queue = deque()
    queue.append((0, 0))
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < row and 0 <= ny < col:
                if maps[nx][ny] == 1:
                    maps[nx][ny] = maps[x][y] + 1
                    queue.append((nx, ny))
                    
    if maps[row-1][col-1] == 1:
        answer = -1
    else:
        answer = maps[row-1][col-1]
    
    return answer
