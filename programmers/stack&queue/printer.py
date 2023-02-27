from collections import deque


def solution(priorities, location):
    answer = 0
    count = 0   # 몇번째로 출력이 되는지 알기 위해 설정한 변수 
    queue = deque() #queue를 사용하기 위해 deque() 사용

    for i, p in enumerate(priorities):
        queue.append((p, i))

    # print(max(queue))
    # print(max(queue)[0])

    while queue:
        # max값일 경우 빼기
        if queue[0][0] == max(queue)[0]:
            count += 1
            # location 일 경우 return
            if queue[0][1] == location:
                return count
            # location이 아닐경우 dequeue()만 진행해주기
            else:
                queue.popleft()
        # max값이 아닐경우 빼서 뒤로 넣어주기
        else:
            queue.append(queue.popleft())

    return answer


print(solution(priorities=[2, 1, 3, 2], location=2))
print(solution(priorities=[1, 1, 9, 1, 1, 1], location=0))
