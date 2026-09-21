from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    
    bridge = deque([0]*bridge_length)
    truck = deque(truck_weights)
    
    while truck:
        bridge.popleft()
        answer += 1
        
        if sum(bridge) + truck[0] <= weight:
            bridge.append(truck.popleft())
        else:
            bridge.append(0)
            
    answer += bridge_length
            
    
    return answer
