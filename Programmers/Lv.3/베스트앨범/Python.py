def solution(genres, plays):
    answer = []
    new_list = []
    
    for i in range(len(genres)):
        new_list.append((genres[i], plays[i], i))
        
    new_list.sort(key=lambda x: (-x[1], x[2]))
    
    frist_genres = {}
    for i in new_list:
        plays_num = int(i[1])
        if i[0] in frist_genres :
            frist_genres[i[0]] += plays_num
        else:
            frist_genres[i[0]] = plays_num
    
    frist_genres = sorted(frist_genres.items(), key = lambda x : x[1], reverse=True)
    
    
    for g, t in frist_genres:
        count = 0
        
        for a, b, index in new_list:
            if g == a:
                answer.append(index)
                count += 1
                
                if count == 2:
                    break
    
    return answer
