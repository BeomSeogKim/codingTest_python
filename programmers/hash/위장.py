# 문제 소스 : https://school.programmers.co.kr/learn/courses/30/lessons/42578?language=python3

def solution(clothes):
    answer = 1
    clothe_hash = {}

    # hash에 의상넣어주기
    for clothe in clothes:
        # hash에 key 값이 존재할 경우 value + 1
        if clothe[1] in clothe_hash:
            clothe_hash[clothe[1]] = clothe_hash.get(clothe[1]) + 1
        # hahs에 key 값이 없을 경우 추가 
        else:
            pass
            clothe_hash[clothe[1]] = 1
    # 전체 의상 경우의 수 = {(의상별 종류 수 + 1) * (의상별 종류 수 + 1) *** } - 1(아예 안입는건 안된다.)
    for clothe in clothe_hash:
        answer = answer * (clothe_hash.get(clothe) + 1)
    answer -= 1
    return answer


print(solution([["yellow_hat", "headgear"], [
      "blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))

print(solution([["crow_mask", "face"], [
      "blue_sunglasses", "face"], ["smoky_makeup", "face"]]))
