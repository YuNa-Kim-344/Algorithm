def solution(video_len, pos, op_start, op_end, commands):
    
    # prev  = 10초 전 이동
    # next = 10초 후 이동
    # op_start <= 현재 재생 위치 =< op_end = 오프닝 끝나는 위치로 이동 
    # video_len = 동영상 길이 문자열 
    # pos = 재생 위치 문자열
    # commands = 사용자의 입력 (1차원 문자열 배열)
    # 사용자 입력 완료 -> return 값 mm : ss
    
    # time 문자열 숫자로 (초) 변경 
    def time_sec(time):
        minute, second = time.split(":")
        
        minute = int(minute)
        second = int(second)
        
        pos_sec = minute * 60 + second
        return pos_sec
        
    # 숫자 (초) time 문자열로 변경 
    def sec_time(pos_sec):
        minute = int(pos_sec) // 60
        second = int(pos_sec) % 60 
        
        min_sec = f"{minute:02d}:{second:02d}"
        
        return min_sec
    
    
    video_len_sec = time_sec(video_len)
    pos_sec = time_sec(pos)
    op_start_sec = time_sec(op_start)
    op_end_sec = time_sec(op_end)
    
    
    
    def prev(pos_sec) :
        
        max_sec = max(0, pos_sec - 10)
        
        return max_sec
        
    def next(pos_sec) :
        
        min_sec = min(video_len_sec, pos_sec + 10)
        
        return min_sec
    
    
    for command in commands:
         # 오프닝 건너뛰기    
        if op_start_sec <= pos_sec <= op_end_sec:
            pos_sec = op_end_sec
        
        if command == "prev":
            pos_sec = prev(pos_sec)
        elif command == "next":
            pos_sec = next(pos_sec)
        else:
            print("틀리묘 : ", command)

        # 오프닝 건너뛰기    
        if op_start_sec <= pos_sec <= op_end_sec:
            pos_sec = op_end_sec
            
            

    answer = sec_time(pos_sec)
    
    return answer
