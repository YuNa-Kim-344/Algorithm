def solution(elements):
    answer = 0
    list = []
    
    length = len(elements)
    circle = elements + elements
    
    for i in range(length):
        for j in range(length):
            list.append(sum(circle[i:j+i]))
            
    answer = len(set(list))
    
    return answer
