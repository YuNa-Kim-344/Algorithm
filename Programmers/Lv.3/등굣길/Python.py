def solution(m, n, puddles):
    answer = 0
    
    # n = 행  / m = 열 
    # 문제 좌표 순서 m, n = 열, 행 = c, r
    dp = [[0 for _ in range(m)] for _ in range(n)]
    
    for c, r in puddles:
        dp[r-1][c-1] = -1
    
    # print(dp)
    
    dp[0][0] = 1
    
    for r in range(n): # 행
        for c in range(m): # 열
            # 웅덩이
            if dp[r][c] == -1:
                continue
            # 시작점
            if r == 0 and c == 0:
                continue
            # 위에서 오는 경우
            if r>0 and dp[r-1][c] != -1:
                dp[r][c] += dp[r-1][c]
            # 왼쪽에서 오는 경우
            if c>0 and dp[r][c-1] != -1:
                dp[r][c] += dp[r][c-1]
                
    answer = dp[n-1][m-1] % 1000000007
    
    return answer
