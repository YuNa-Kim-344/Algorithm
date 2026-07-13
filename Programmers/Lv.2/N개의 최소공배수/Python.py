def solution(arr):
    answer = 1
    
    def make_gcd(i, j):
        while j > 0:
            i, j = j, i%j
        return i
            
    def make_lcm(i, j):
        # lcm = (i * j) // gcd
        return (i * j) // make_gcd(i, j)
    
    for i in arr:
        answer = make_lcm(answer, i)
    
    return answer
