def solution(want, number, discount):
    answer = 0
    
    for i in range(len(discount)-9):
        check = discount[i:i+10]
        
        is_possible = True
        
        for j in range(len(want)):
            if check.count(want[j]) != number[j]:
                is_possible = False
                break
                
        if is_possible == True:
            answer += 1
                
    return answer
