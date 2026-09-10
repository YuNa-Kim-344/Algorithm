def solution(numbers):
    answer = []
    
    for num in numbers:
        if num % 2 == 0:
            answer.append(num+1)
        else:
            bit = '0' + format(num, 'b')
            idx = bit.rfind('0')
            different_bit = bit[:idx] + '10' + bit[idx+2:]
        
            answer.append(int(different_bit, 2))
    
    return answer
