def solution(clothes):
    answer = 1
    
    new = {}
    for i in range(len(clothes)):
        if clothes[i][1] in new:
            new[clothes[i][1]].append(clothes[i][0])
        else:
            new[clothes[i][1]] = [clothes[i][0]]
            
    
    for i in new.values():
        answer *= len(i) + 1
    
    answer += -1
            
    return answer
