def solution(brown, yellow):
    answer = []

    carpet = brown + yellow
    
    for i in range(1, carpet):
        if carpet % i == 0:
            a = carpet//i
            b = i
            
        if a >= b and (a-2) * (b-2) == yellow:
            answer = [a, b]
    
    return answer
