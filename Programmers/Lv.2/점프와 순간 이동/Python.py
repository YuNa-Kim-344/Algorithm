def solution(n):
    ans = 0 # 배터리 사용량
    # n = 가야 할 거리
    
    while n > 0:
        if n%2 == 0:
            n //= 2
        else:
            n -= 1
            ans += 1
            
    return ans
