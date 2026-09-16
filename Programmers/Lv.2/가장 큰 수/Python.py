def solution(numbers):
    answer = ''

    numbers = [str(i) for i in numbers]
    
    numbers.sort(key=lambda x:x*3, reverse=True)
        
    for i in range(len(numbers)):
        answer += numbers[i]
        
    if answer[0] == '0':
        return '0'    
    
    return answer
