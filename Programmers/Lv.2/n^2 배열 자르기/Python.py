def solution(n, left, right):
    answer = []
    
    for i in range(left, right+1):
        row = i // n
        col = i % n
        
        answer.append(max(row, col) + 1)
    
    
#     n_arr2 = []
#     for i in range(1, n+1):
#         row = []
#         for j in range(1, n+1):
#             row.append(max(i, j))
#         n_arr2.append(row)
        
#     n_arr1 = []
#     for i in n_arr2:
#         n_arr1 += i
    
#     for i in range(len(n_arr1)):
#         if i >= left and i<= right:
#             answer.append(n_arr1[i])
    
    return answer
