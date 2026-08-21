def solution(n, k):
    answer = 0
    
    def convert(n, k):
        chars = "0123456789ABCDEF"
        
        if n == 0:
            return 0
        
        result = ""
        
        while n > 0:
            result = chars[n%k] + result
            n //= k
            
        return result
    
    num_list = convert(n, k).split("0")
    
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    for i in num_list:
        if i and is_prime(int(i)):
            answer += 1
    
    return answer
