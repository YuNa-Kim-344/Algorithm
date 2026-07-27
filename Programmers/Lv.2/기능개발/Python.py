def solution(progresses, speeds):
    answer = []
    
    done = []
    
    for i in range(len(progresses)):
        num = 100 - progresses[i]
        count =  (num + speeds[i] - 1) // speeds[i]
        done.append(count)
    
    i = 0
    while i < len(done):
        count = 1
        j = i+1
        while j < len(done):
            if done[i] < done[j]:
                break
            else:
                count += 1
                j += 1
        answer.append(count)
        i = j
        
    return answer
