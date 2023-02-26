# 문제 소스 : https://school.programmers.co.kr/learn/courses/30/lessons/42579?language=python3

def solution(genres, plays):
    answer = []

    dic1 = {}   # 각 앨범의 플레이 횟수
    dic2 = {}   # 각 장르별 플레이 총합

    for index, (genre, play) in enumerate(zip(genres, plays)):
        if genre not in dic1:
            dic1[genre] = [(index, play)]
        else:
            dic1[genre].append((index, play))

        if genre not in dic2:
            dic2[genre] = play
        else:
            dic2[genre] += play

    for (key, value) in sorted(dic2.items(), key=lambda x: x[1], reverse=True):
        for (index, play) in sorted(dic1[key], key=lambda x: x[1], reverse=True)[:2]:
            answer.append(index)

    return answer


print(solution(genres=["classic", "pop", "classic",
      "classic", "pop"], plays=[500, 600, 150, 800, 2500]))
