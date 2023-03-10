# 문제 소스 : https://school.programmers.co.kr/learn/courses/30/lessons/42747?language=python3

def solution(citations):
    answer = 0
    # 내림차순 정렬
    citations.sort(reverse=True)

    for index, number in enumerate(citations):
        # 만약 index가 number보다 크게 되면 
        # 그 index가 h-value 이다.
        if index >= number:
            return index
    # 전체가 다 통과할 경우 h-index는 citation의 길이 만큼.
    return len(citations)
