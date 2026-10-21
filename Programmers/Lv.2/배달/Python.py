import heapq

def solution(N, road, K):
    answer = 0
    
    graph = [[] for _ in range(N + 1)]
    for a, b, cost in road:
        graph[a].append((b, cost))
        graph[b].append((a, cost))
    
    def dijkstra(start):
        distance = [float('inf')]*(N+1)
        
        q = []
        heapq.heappush(q, (0, start))
        distance[start] = 0
        
        while q:
            dist, now = heapq.heappop(q)
            
            if dist > distance[now]:
                continue
                
            for next, cost in graph[now]:
                new_dist = dist + cost
                
                if new_dist < distance[next]:
                    distance[next] = new_dist
                    heapq.heappush(q, (new_dist, next))
        
        return distance
    
    distance = dijkstra(1)

    for dist in distance[1:]:
        if dist <= K:
            answer += 1
    
    return answer
