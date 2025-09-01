def solution(n):
    answer = []
    while n > 0:
        a = int(n%10)
        answer.append(a)
        n = int(n/10)
    return answer
