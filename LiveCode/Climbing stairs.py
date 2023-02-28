# 문제 소스 : https://leetcode.com/problems/climbing-stairs/
# dp 
#  1. topwdown  => 재귀를 이용한 방식 + memoization
#  2. bottom up => 반복문을 이용한 방식 
def solution(n):
    memo = {}
    
    def dp(n):
        # base case 
        if n == 1:
            memo[1] = 1
            return 1
        if n == 2:
            memo[2] = 2
            return 2
        
        if n not in memo:
            memo[n] = solution(n-1) + solution(n-2)
    
        return memo[n] 
    return dp(n)

print(solution(40))

