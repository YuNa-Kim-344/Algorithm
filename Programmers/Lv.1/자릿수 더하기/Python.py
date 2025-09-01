def solution(n):
    answer = 0

    while n > 0:
        i = n%10
        answer += i
        n = n//10

    return answer
