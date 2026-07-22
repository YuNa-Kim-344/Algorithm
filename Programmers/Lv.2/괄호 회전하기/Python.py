def solution(s):
    answer = 0
    new_s = s + s
    
    for i in range(len(s)):
        check = new_s[i:i+len(s)]
        stack = []
        is_possible = True
        
        for j in check:
            if j == "(" or j == "{" or j == "[":
                stack.append(j)
            else:
                if not stack:
                    is_possible = False
                    break
                    
                if j == ")" and stack.pop() != "(":
                    is_possible = False
                    break
                elif j == "}" and stack.pop() != "{":
                    is_possible = False
                    break
                elif j == "]" and stack.pop() != "[":
                    is_possible = False
                    break
                
        if is_possible and not stack:
            answer += 1
    
    return answer
