def solution(k, tangerine):
    answer = 0
    
    count_num = {}
    
    for i in tangerine:
        if i in count_num:
            count_num[i] += 1
        else:
            count_num[i] = 1
        
    count_list = list(count_num.values())
    count_list.sort(reverse = True)
        
    for i in count_list:
        k -= i
        answer += 1
        
        if k <= 0:
            break
    
    return answer
  
