def solution(sequence, k):
    answer = []
    
    totel = 0
    j = 0
    
    for i in range(len(sequence)):
        totel += sequence[i]
        
        while totel > k:
            totel -= sequence[j]
            j += 1
            
        if totel == k:
            if not answer or i - j < answer[1] - answer[0]:
                answer = [j, i]
                
    
    return answer
