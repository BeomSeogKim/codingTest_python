# 문제 소스 : https://school.programmers.co.kr/learn/courses/30/lessons/42840?language=python3

def solution(answers):
    answer = []
    s1 = [1, 2, 3, 4, 5]
    s2 = [2, 1, 2, 3, 2, 4, 2, 5]
    s3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    answer_s1 = 0
    answer_s2 = 0
    answer_s3 = 0
    for index, value in enumerate(answers):
        # s1 count
        if s1[index % 5] == value:
            answer_s1 += 1
        # s2 count
        if s2[index % 8] == value:
            answer_s2 += 1
        # s3 count
        if s3[index % 10] == value:
            answer_s3 += 1
    max_answer = max(answer_s1, answer_s2, answer_s3)
    if answer_s1 == max_answer:
        answer.append(1)
    if answer_s2 == max_answer:
        answer.append(2)
    if answer_s3 == max_answer:
        answer.append(3)
    return answer
print(solution([1,2,3,4,5]))
print(solution([1,3,2,4,2]))