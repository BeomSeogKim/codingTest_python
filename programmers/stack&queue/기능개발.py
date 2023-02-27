import math


def solution(progresses, speeds):
    answer = []
    process = []
    for (p, s) in zip(progresses, speeds):
        # 작업에 총 걸리는 시간을 추출
        time = math.ceil((100 - p) / s)
        process.append(time)
    count = 0
    work_time = process[0]
    print(process)
    for p in process:
        # 기존의 time 보다 작을 경우는 count++
        # 기존의 time 보다 높을 경우는 answer에 count 를 넣고 count 초기화
        if work_time > p or work_time == p:
            count += 1
        else:
            work_time = p
            answer.append(count)
            count = 1

    answer.append(count)
    return answer


print(solution(progresses=[93, 30, 55], speeds=[1, 30, 5]))

