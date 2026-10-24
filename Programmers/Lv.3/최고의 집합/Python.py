def solution(n, s):
    answer = []
    
    if n > s:
        return [-1]
    
    A = s//n # 몫
    B = s%n # 나머지
    
    for i in range(n-B):
        answer.append(A)
    for j in range(B) :
        answer.append(A+1)
    
    return answer
