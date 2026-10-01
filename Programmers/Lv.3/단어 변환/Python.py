def solution(begin, target, words):
    answer = 0
    
    visited = [False] * len(words)
    
    def dfs(now_word, count):
        nonlocal answer
        
        if now_word == target:
            answer = count
            return answer
        
        
        for i in range(len(words)):
            if not visited[i]:
                diff = 0 # 다른 글자 수
                
                for j in range(len(now_word)):
                    if now_word[j] != words[i][j]:
                        diff += 1
                print(now_word, words[i], diff)
                        
                if diff == 1:
                    visited[i] = True
                    dfs(words[i], count + 1)
                    visited[i] = False
                    
    dfs(begin, 0)
    
    return answer
