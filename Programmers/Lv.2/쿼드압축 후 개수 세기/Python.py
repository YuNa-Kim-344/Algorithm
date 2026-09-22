def solution(arr):
    answer = []
    zero = 0
    one = 0
    
    for i in arr:
        zero += i.count(0)
        one += i.count(1)
        
    print(zero, one)
    row= len(arr)
    
    def check(r, c, size):
        nonlocal zero
        nonlocal one
        
        value = arr[r][c]
        same = True

        for i in range(r, r+size):
            for j in range(c, c+size):
                if arr[i][j] != value:
                    same = False
                    break
            if not same:
                break
                    
        
        if same:
            if value == 0:
                zero -= (size * size)-1
            else:
                one -= (size * size)-1
            return
        
        h = size // 2
        
        check(r, c, h)
        check(r, c+h, h)
        check(r+h, c, h)
        check(r+h, c+h, h)
    
    check(0, 0, row)
        
    answer = [zero, one]
    
    return answer
