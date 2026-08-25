def solution(skill, skill_trees):
    answer = 0
    
    skill = list(skill)
    
    for i in skill_trees:
        skill_i = 0
        s = 0 
        print(i)
        for j in i: 
            if j in skill and j == skill[skill_i]:
                skill_i += 1
                s += 1
            elif j in skill and j != skill[skill_i]:
                break
            else:
                s += 1
                
        if s == len(i):
            answer += 1
    
    return answer
