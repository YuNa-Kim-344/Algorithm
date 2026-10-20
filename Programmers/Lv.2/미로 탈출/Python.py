from collections import deque

def solution(maps):
    answer = 0
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1] # 위, 아래, 왼, 오
    
    for r in range(len(maps)):
        for c in range(len(maps[r])):
            if maps[r][c] == "S":
                S_index = [r, c]
            elif maps[r][c] == "E":
                E_index = [r, c]
            elif maps[r][c] == "L":
                L_index = [r, c] 

    def bfs(start, target):
        
        visited = [list(row) for row in maps]
    
        for r in range(len(visited)):
            for c in range(len(visited[r])):
                if visited[r][c] == "X":
                    visited[r][c] = True
                else:
                    visited[r][c] = False # 아직 방문 안 함
                    
        q = deque()
        q.append((start[0], start[1], 0))
        visited[start[0]][start[1]] = True
        
        while q:
            x, y , count = q.popleft()
            
            if [x, y] == target:
                return count
            
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                
                if 0 <= nx < len(maps) and 0 <= ny < len(maps[0]):
                    if maps[nx][ny] != "X" and not visited[nx][ny]:
                        visited[nx][ny] = True
                        q.append((nx, ny, count + 1))
    
        return -1

    S_to_L = bfs(S_index, L_index)

    if S_to_L == -1:
        return -1

    L_to_E = bfs(L_index, E_index)

    if L_to_E == -1:
        return -1

    answer = S_to_L + L_to_E
    
    return answer
