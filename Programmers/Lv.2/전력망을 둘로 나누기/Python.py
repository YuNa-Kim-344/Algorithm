def solution(n, wires):
    answer = n
    
    for cut_a, cut_b in wires:
        
        visited = [False] * (n+1)
        
        def dfs(now):
            visited[now] = True
            count = 1
            
            for a, b in wires:
                
                if (a == cut_a and b == cut_b) or (a == cut_b and b == cut_a):
                    continue
                if a == now and not visited[b]:
                    count += dfs(b)
                if b == now and not visited[a]:
                    count += dfs(a)
                    
            return count
    
        left = dfs(1)
        right = n - left
    
        answer = min(answer, abs(left-right))
    
    return answer
