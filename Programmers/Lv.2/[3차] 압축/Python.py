def solution(msg):
    answer = []
    
    words = ["A", "B", "C", "D", "E", 
             "F", "G", "H", "I", "J", 
             "K", "L", "M", "N", "O",
             "P", "Q", "R", "S", "T", 
             "U", "V", "W", "X", "Y", "Z"]
    
    i = 0
    
    while i < len(msg):
        j = i + 1
        
        while j <= len(msg) and msg[i:j] in words:
            j += 1
        
        answer.append(words.index(msg[i:j-1])+1)
        
        if j <= len(msg):
            words.append(msg[i:j])
         
        i += len(msg[i:j-1])
    
    return answer
