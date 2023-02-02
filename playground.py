class Solution(object):

    def twoSum_nSqure(nums, target):
        n_length = len(nums)
        for i in range(n_length):
            for j in range (i +1, n_length):
                if(nums[i] + nums[j] == target):
                    return [i,j]
                    
    def twoSum(nums, target):
        nums = [[n, i] for i, n in enumerate(nums)] # i 에는 index, n 에는 value
        nums.sort(key = lambda x : x[0])    # 오름 차순 정렬 
        l, r = 0, len(nums) - 1 
        while l <= r:
            num_sum = nums[l][0] +nums[r][0]
            if num_sum == target:
                return [nums[l][1], nums[r][1]]
            elif num_sum >= target:
                r -= 1
            else:
                l += 1

    print(twoSum(nums = [2,7,11,15], target = 9))
