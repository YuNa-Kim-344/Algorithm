def solution(record):
    answer = []
    
    user = {}
    
    for i in range(len(record)):
        record[i] = record[i].split(' ')
        
        if record[i][1] not in user:
            user[record[i][1]] =  record[i][2]
        
        if record[i][0] == 'Enter':
            answer.append([record[i][1], "님이 들어왔습니다."])
            user[record[i][1]] =  record[i][2]
        elif record[i][0] == 'Leave':
            answer.append([record[i][1], "님이 나갔습니다."])
        else:
            user[record[i][1]] =  record[i][2]
            
    for i in range(len(answer)):
        answer[i][0] = user[answer[i][0]]
        answer[i] = answer[i][0] + answer[i][1]
    
    return answer
