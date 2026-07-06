def solution(n):
    answer = 0
    
    bin_n = format(n, 'b')
    
    for i in range(n+1, 10000000):
        bin_i = format(i, 'b')
        if bin_n.count("1") == bin_i.count("1"):
            answer = i
            break
            
    return answer
