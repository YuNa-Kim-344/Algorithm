def solution(arr):
    answer = []
    
    if len(arr) > 1 :
        arr_min = min(arr)   
        arr.remove(arr_min)
        answer = arr
    else :
        return [-1]
    
    return answer
