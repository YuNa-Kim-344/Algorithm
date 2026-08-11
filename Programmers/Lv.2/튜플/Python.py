def solution(s):
    answer = []
    
    new = s[2:-2].split("},{")
    list_s = [list(map(int, i.split(","))) for i in new ]
    
    list_s.sort(key=len)
    
    for nums in list_s:
        for num in nums:
            if num not in answer:
                answer.append(num)
              
#     list_s = new.split("},{") 
#     i = 1
    
#     while i <= len(list_s):
#         for j in range(len(list_s)):
#             nums = list(map(int, list_s[j].split(",")))
            
#             if len(nums) == i:
#                 for k in nums:
#                     if k not in answer:
#                         answer.append(k)
                        
#         i += 1
    
    return answer
