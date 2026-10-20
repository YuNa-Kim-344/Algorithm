def solution(n):
    answer = []
        
    tree = []
    for j in range(1, n+1):
        tree.append([False]*j)
        
    r = -1
    c = 0
    num = 1
    for d in range(n):
        move = n - d
        
        for _ in range(move):
            if d % 3 == 0:
                r += 1 # 아래
            elif d % 3 == 1:
                c += 1 # 오른쪽
            else:
                r -= 1
                c -= 1
                # 대각선

            tree[r][c] = num
            num += 1
    
    for i in tree:
        answer += i
    

    return answer
