def solution(n):
    answer = 0
    
    def change_ternary(n):
        ternary_num = ''
        while n>0:
            ternary_num = str(n%3) + ternary_num
            n//=3
        return ternary_num
    
    def reversal(n):
        return n[::-1]
    
    def change_decimal(n):
        return int(n, 3)
    
    ternary_num = change_ternary(n)
    reversal_num = reversal(ternary_num)
    answer = change_decimal(reversal_num)
    
    return answer
