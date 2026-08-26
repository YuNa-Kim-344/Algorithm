def solution(n):
    answer = 0
    
    # 1 과 2로 n 을 만들 수 있는 경우의 수 구하기.
    
    if n == 1:
        return 1
    
    a = 1
    b = 2
    
    for i in range(3, n+1):
        a, b = b, (a+b)
    
    
    answer = b % 1000000007
    
    return answer
