def solution(topping):
    answer = 0
    
    left = set()
    right = {}
    
    for i in topping:
        if i in right:
            right[i] += 1
        else:
            right[i] = 1
            
    for j in topping:
        left.add(j)
        right[j] -= 1
        
        if right[j] == 0:
            del right[j]
            
        if len(left) == len(right):
            answer += 1
    
    # for i in range(1, len(topping)):
    #     left = topping[0:i]
    #     right = topping[i:]
    #     if len(set(left)) == len(set(right)):
    #         answer +=1
    
    return answer
