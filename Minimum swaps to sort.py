class Solution:
    def minSwaps(self, nums):
        dic = {i: index for index, i in enumerate(nums)}
        sortted = sorted(nums)
        num = 0
        for i in range(len(nums)):
            if sortted[i] != nums[i]:
                pos = dic[sortted[i]]
                nums[i], nums[pos] = nums[pos], nums[i]
                dic[nums[i]],dic[nums[pos]] = dic[nums[pos]], dic[nums[i]]
                num += 1
        return num


nums = [7, 16, 14, 17, 6, 9, 5, 3, 18]
obj = Solution()
ans = obj.minSwaps(nums)
print(ans)
