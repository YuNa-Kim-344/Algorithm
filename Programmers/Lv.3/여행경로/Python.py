def solution(tickets):
    answer = ["ICN"]
    
    tickets.sort(key = lambda x : x[1])
    
    visited = [False] * len(tickets)
    
    def dfs(now):
        nonlocal answer
        
        if len(answer) == len(tickets)+1:
            return answer
        
        for i in range(len(tickets)):
                start, end = tickets[i]

                if not visited[i] and start == now:
                    visited[i] = True
                    answer.append(end)
                    
                    if dfs(end):
                        return True

                    answer.pop()
                    visited[i] = False

    
    dfs("ICN")
    
    return answer
