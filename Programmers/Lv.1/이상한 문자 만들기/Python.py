def solution(s):
    answer = ''
    
    for word in s.split(" "):
        new_word = ''
        for i in range(len(word)):
            if i%2==0:
                new_word += word[i].upper()
            else:
                new_word += word[i].lower()
            
        answer += new_word + " "
    
    answer = answer.rstrip()
    
    return answer
