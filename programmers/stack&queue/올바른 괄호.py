# 문제 소스 : https://school.programmers.co.kr/learn/courses/30/lessons/12909?language=python3

def solution(s):
    answer = False
    # let a = stack
    a = []
    # (일 경우 a에 대입, )일 경우 a에서 pop
    for t in s:
        if t == "(":
            a.append(t)
        else:
            # 만약 처음부터 ) 가 들어올 경우 => False
            if (len(a) == 0):
                return False
            else:
                a.pop()
    # 모든 loop를 돈 후에 stack이 비어있다면 True
    if len(a) == 0:
        answer = True
    return answer


print(solution("(()("))
print(solution("(())()"))
