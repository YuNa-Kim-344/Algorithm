def solution(files):
    answer = []
    
    for f in range(len(files)):
        file = files[f]
        
        i = 0

        while not file[i].isdigit():
            i += 1

        head = file[:i]
        
        j = i
        
        while j < len(file) and file[j].isdigit():
            j += 1
            
        number = file[i:j]

        answer.append([head, int(number), file])
    
    answer.sort(key=lambda x: (x[0].lower(), x[1]))
    
    for i in range(len(answer)):
        answer[i] = answer[i][2] 
    
    print(answer)
    
    return answer
