def solution(book_time):
    answer = 0
    
    use_room = []
    book_time.sort()
    print(book_time)
    
    def clock(a):
        h, m = map(int, a.split(':'))
        return h*60 + m
    
    for i in book_time:
        used = False
            
        for j in range(len(use_room)):
            if use_room[j] <= clock(i[0]):
                use_room[j] = clock(i[1]) + 10
                used = True
                break
                
        if not used:
            use_room.append(clock(i[1])+10) # 이용중, 청소 완료 시간
            
    answer = len(use_room)
    
    return answer
