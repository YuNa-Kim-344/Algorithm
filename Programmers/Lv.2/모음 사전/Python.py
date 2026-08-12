def solution(word):
    answer = 0
    
    list_word = list(word)
    
    weight = [781, 156, 31, 6, 1]
    
    for i in range(len(list_word)):
        if list_word[i] == "A":
            answer = answer + weight[i]*0 + 1
        elif list_word[i] == "E":
            answer = answer + weight[i]*1 + 1
        elif list_word[i] == "I":
            answer = answer + weight[i]*2 + 1
        elif list_word[i] == "O":
            answer = answer + weight[i]*3 + 1
        else:
            answer = answer + weight[i]*4 + 1
        
        print(answer)
    
    return answer
