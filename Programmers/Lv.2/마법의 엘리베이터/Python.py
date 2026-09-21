def solution(storey):
    answer = 0
    
    while storey > 0:
        n = storey%10
        storey //= 10
        
        if n < 5:
            answer += n
        elif n == 5:
            next_n = storey%10
            if next_n >= 5:
                answer += 5
                storey += 1
            else:
                answer += 5
        else:
            answer += (10-n)
            storey += 1
        
    return answer
