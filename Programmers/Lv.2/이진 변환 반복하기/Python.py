def solution(s):
    answer = []
    
    # [A, B] A: 이진 변환 횟수, B: 제거한 0의 총 개수
    A = 0
    B = 0
    
    while s != "1":
        count_0 = s.count("0")
        B += count_0
        
        new_s = s.replace("0", "")
        A += 1
        
        s = format(len(new_s), 'b')
        
    answer = [A, B]
    
    return answer
