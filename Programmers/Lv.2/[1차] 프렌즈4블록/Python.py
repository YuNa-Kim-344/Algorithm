def solution(m, n, board):
    answer = 0
    
    board = [list(row) for row in board]
    
    use = set()
    
    while True:
        
        # 2x2 찾아서 use에 위치 넣기
        for x in range(m-1):
            for y in range(n-1):
                if (board[x][y] != 0
                    and board[x][y] == board[x][y+1] 
                    and board[x][y] == board[x+1][y] 
                    and board[x][y] == board[x+1][y+1]
                   ):
                    use.add((x, y))
                    use.add((x, y+1))
                    use.add((x+1, y))
                    use.add((x+1, y+1))
                    
        if not use:
            break

        # 겹치는 위치 삭제
        for x, y in use:
            board[x][y] = 0

        # 비어있는 곳에 내리기
        for i in range(1, m):
            for j in range(n):
                if board[i][j] == 0:
                    board[i][j] = board[i-1][j]
                    board[i-1][j] = 0
                    
        for y in range(n):
            for x in range(m-1, 0, -1):
                if board[x][y] == 0:
                    k = x - 1
                    while k >= 0 and board[k][y] == 0:
                        k -= 1
                        
                    if k >= 0:
                        board[x][y] = board[k][y]
                        board[k][y] = 0

        answer += len(use)
        use = set()
    
    return answer
