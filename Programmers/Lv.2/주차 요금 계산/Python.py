def solution(fees, records):
    answer = []
    
    total_time = {}
    
    for i in range(len(records)):
        records[i] = records[i].split(" ")
        
        records[i][0] = records[i][0].split(":")
        records[i][0] = int(records[i][0][0]) * 60 + int(records[i][0][1])
            
            
    for time, car, inout in records:
        if car not in total_time:
            total_time[car] = 0
            
        if inout == "IN":
            total_time[car] -= time
        else:
            total_time[car] += time
            
    total_time = sorted(total_time.items())
            
    for car, time in total_time:
        if time <= 0:
            time += 23*60 + 59
            print(time)
        
        if time > fees[0]:
            use = ((time-fees[0]) + fees[2] - 1)//fees[2]
            answer.append(fees[1] + use*fees[3])
        else:
            answer.append(fees[1])
                
    return answer
