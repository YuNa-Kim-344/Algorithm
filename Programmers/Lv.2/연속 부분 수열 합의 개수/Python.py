def solution(elements):
    answer = 0
    list = []
    
    length = len(elements)
    circle = elements + elements
    
    for i in range(length):
        for j in range(1, length + 1):
            list.append(sum(circle[i:i+j]))
            
    answer = len(set(list))
    
    return answer
