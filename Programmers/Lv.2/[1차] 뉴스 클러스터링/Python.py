def solution(str1, str2):
    answer = 0
    
    str1 = str1.lower()
    str2 = str2.lower()
    
    A = []
    B = []
    
    for i in range(len(str1)-1):
        word = str1[i:i+2]
        
        if word.isalpha():
            A.append(word)
    
    for i in range(len(str2)-1):
        word = str2[i:i+2]
        
        if word.isalpha():
            B.append(word)

    def J(A, B):
        # J = 교집합 / 합집합
        # 교집합 = 겹치는 문자열
        # 합집합 = 두 문자열 합에서 겹치는(중복) 뺀 문자열들
        
        if len(A) == 0 and len(B) == 0:
            return 1
        
        B_copy = B.copy()
        rywlqgkq = 0 # 교집합 개수

        for i in A:
            if i in B_copy:
                rywlqgkq += 1
                B_copy.remove(i)
    
        return rywlqgkq / (len(A) + len(B) - rywlqgkq)
    
    answer = int(J(A, B) * 65536)
        
    return answer
