def solution(weights):
    answer = 0
    
    weights.sort()
    
    count = {}
    
    for i in weights:
        
        if i in count:
            answer += count[i]
            
        # 2:3
        if i*2%3 == 0:
            target = i*2//3
            if target in count:
                answer += count[target]
                
        # 2:4 = 1:2
        if i%2 == 0:
            target = i//2
            if target in count:
                answer += count[target]
            
        # 3:4
        if i * 3 % 4 == 0:
            target = i * 3 // 4
            if target in count:
                answer += count[target]
        
    
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
            
    print(count)
    
    return answer
