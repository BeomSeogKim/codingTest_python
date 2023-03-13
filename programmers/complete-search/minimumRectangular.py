# 문제 소스 : https://school.programmers.co.kr/learn/courses/30/lessons/86491?language=python3

def solution(sizes):
    answer = 0
    new_card = []
    l_max = 0
    l_min = 0
    for size in sizes:
        if size[0] > size[1]:
            min_size = size[1]
            max_size = size[0]
        else:
            min_size = size[0]
            max_size = size[1]
        new_card.append((min_size, max_size))

    for card in new_card:
        if card[0] > l_min:
            l_min = card[0]
        if card[1] > l_max:
            l_max = card[1]
    answer = l_min * l_max
    return answer


def solution2(sizes):
    # 위 풀이를 간단하게 한 줄로 풀이 한 것.
    return max(max(x) for x in sizes) * max(min(x) for x in sizes)


print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]))
print(solution2([[60, 50], [30, 70], [60, 30], [80, 40]]))
