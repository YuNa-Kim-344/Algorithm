def solution(triangle):
    answer = 0
    
    dp = [row[:] for row in triangle]
    
    for i in range(1, len(dp)):
        for j in range(len(dp[i])):
            if j == 0:
                dp[i][j] += dp[i-1][j]
            elif j == i:
                dp[i][j] += dp[i-1][j-1]
            else:
                dp[i][j] += max(dp[i-1][j], dp[i-1][j-1])
        
    answer = max(dp[-1])
    
    return answer
