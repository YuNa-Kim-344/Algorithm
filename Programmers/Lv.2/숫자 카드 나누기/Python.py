def solution(arrayA, arrayB):
    answer = 0

    arrayA.sort()
    arrayB.sort()
    
    def gcd(a, b):
        while b > 0:
            a, b = b, a%b
        return a
    
    # a 전체 최대 공약수 
    a_gcd = arrayA[0]
    
    for i in arrayA[1:]:
        a_gcd = gcd(a_gcd, i)
        
    # b 전체 최대 공약수 
    b_gcd = arrayB[0]
    
    for i in arrayB[1:]:
        b_gcd = gcd(b_gcd, i)
        
    # a_gcd가 b를 나누는기
    a_b = True
    
    for i in arrayB:
        if i % a_gcd == 0:
            a_b = False
            break
            
    if a_b:
        answer = a_gcd
    
    # b_gcd가 a를 나누는기
    b_a = True
    
    for i in arrayA:
        if i % b_gcd == 0:
            b_a = False
            break
    
    if b_a:
        answer = max(a_gcd, b_gcd)
    
    return answer
