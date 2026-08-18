def solution(n, t, m, p):
    result = ''
    answer = ''
    i = 0
    
    def convert(num, n):
        chars = "0123456789ABCDEF"
        
        if num == 0:
            return "0" 
        
        result = ""
        
        while num > 0:
            result = chars[num % n] + result    
            num //= n
            
        return result
      
    while len(result) != t:
        answer += convert(i, n)
        
        if len(answer) >= p:
            result += answer[p-1]
            p += m
        
        i += 1
           
    return result
