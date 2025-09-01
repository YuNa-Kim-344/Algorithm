def solution(mats, park):
    answer = -1
    mats.sort(reverse=True) # 돗자리 내림차순 정리 
    
    row = len(park) # 공원 열 길이 
    column = len(park[0]) # 공원 행 길이 
    
    for mat_size in mats :
        for i in range(row) : # row 는 int 이기에 반복 불가 -> 정수 리스트 생성 위한 range 사용
            for j in range(column) :
                if park[i][j] == "-1" :
                    if i + mat_size <= row and j + mat_size <= column:  # 공원 범위 초과 방지
                        
                        # case 1
#                             can_place = True
#                             for x in range(i, i + mat_size):
#                                 for y in range(j, j + mat_size):
#                                     if park[x][y] != "-1":  # -1 이 아니면 배치 불가
#                                         can_place = False
#                                         break
#                                 if not can_place:
#                                     break

#                             if can_place:
#                                 return mat_size  # 가장 큰 크기를 찾으면 즉시 반환
                        # case 2
                        # 돗자리 배치 가능 여부 확인
                        for x in range(i, i + mat_size):
                            for y in range(j, j + mat_size):
                                if park[x][y] != "-1":  # 하나라도 -1이 아니면 배치 불가능
                                    break
                            else:
                                continue  # 내부 루프가 정상적으로 끝나면 외부 루프 계속
                            break  # 내부 루프에서 break가 발생하면 외부 루프도 중단
                        else:
                            return mat_size  # 모든 칸이 비어있다면 즉시 반환


    return answer
