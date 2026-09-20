def solution(numbers):
    answer = 0
    
    num_list = list(numbers)
    
    def is_prime(n):
        if n < 2:
            return False
        
        for i in range(2, int(n ** 0.5)+1):
            if n%i == 0:
                return False
        
        return True
    
    made_num = set() # 만든 숫자
    
    def bfs(N, numbers): # 붙일 숫자, 사용 안한 숫자
        
        for i in range(len(numbers)):
            new_num = N + numbers[i]
            made_num.add(int(new_num))
            
            bfs(new_num, numbers[:i]+numbers[i+1:])
        
    bfs("", numbers)
    
    for i in made_num:
        if is_prime(i):
            answer += 1
    
    return answer
