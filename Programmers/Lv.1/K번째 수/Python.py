def solution(array, commands):
    answer = []
    
    for commands in commands:
        i, j, k = commands
        new_array = array[i-1:j]
        new_array.sort()
        answer.append(new_array[k-1])
    
    return answer
