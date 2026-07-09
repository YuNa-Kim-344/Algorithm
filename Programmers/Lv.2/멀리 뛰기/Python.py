def solution(n):
    
    answer = 0
    
    # DP 활용 (동적 계획법 = 이미 계산한 값을 저장해두고, 다시 필요할 때 재사용하는 방법)
    
    dp = [0] * (n + 1)
    
    dp[0] = 1
    dp[1] = 1
    
    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    
    answer = dp[n] % 1234567
    
    
#  재귀함수 방식 -> 시간 초과
    
#     def RF(totel, path):
#         nonlocal answer
        
#         if totel == n:
#             print(path)
#             answer += 1
#             return answer % 1234567
        
#         for i in range(1, 3):
#             if totel + i <= n:
#                 RF(totel + i, path + [i])
                
#     RF(0, [])
    
    return answer
