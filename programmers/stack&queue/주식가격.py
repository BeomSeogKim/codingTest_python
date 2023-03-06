# 문제 소스 : https://school.programmers.co.kr/learn/courses/30/lessons/42584?language=python3

def solution(prices):
    # answer 를 0 배열로 초기화
    answer = [0] * len(prices)
    stack = []
    for i in range(len(prices)):
        # stack is not empty & stack[-1] > price
        while stack != [] and stack[-1][1] > prices[i]:
            past_index, _ = stack.pop()
            answer[past_index] = i - past_index

        stack.append((i, prices[i]))
    # index는 0부터 시작 길이는 1부터 시작
    for i, _ in stack:
        answer[i] = len(prices) - i - 1
    return answer


print(solution(prices=[1, 2, 3, 2, 3]))
