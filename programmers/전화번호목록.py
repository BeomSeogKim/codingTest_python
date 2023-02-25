# 문제 소스 : https://school.programmers.co.kr/learn/courses/30/lessons/42577?language=python3

def solution(phone_book):
    answer = True
    phone_hash = {}
    # hash에 모든 전화번호 기재
    for phone_number in phone_book:
        phone_hash[phone_number] = True
    # phone_book 루프
    for phone_number in phone_book:
        temp = ""   # 단어를 담을 곳
        # phone_number 루프 돌기 "123" -> "1" "12" "123"
        for number in phone_number:
            temp += number
            if temp in phone_hash and temp != phone_number:
                return False
    return answer

print(solution(["12","123","1235","567","88"]))
print(solution(["123", "456", "789"]))
print(solution(["119", "97674223", "1195524421"]))
