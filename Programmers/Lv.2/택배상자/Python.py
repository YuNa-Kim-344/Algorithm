def solution(order):
    answer = 0
    
    stack = []
    i = 0 # order의 인덱스
    j = 1 # 이번에 들어오는 택배 상자 번호
    
    while j <= len(order):
        if j == order[i]: 
            answer += 1
            j += 1
            i += 1
            
            if i == len(order): # order 길이가
                return answer
            
        else:
            stack.append(j)
            j += 1
            
        while stack and i < len(order) and stack[-1] == order[i]:
            stack.pop()
            i += 1
            answer += 1
        
    return answer
