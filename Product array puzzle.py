class Solution:
    def productExceptSelf(self, nums, n):
        l = []
        total = 1
        flag = 0

        for i in nums:
            if i != 0:
                total *= i
            else:
                flag += 1

        if flag == 0:
            for i in range(n):
                l.append(total // nums[i])

        elif flag > 1:
            for i in range(n):
                l.append(0)

        else:
            for i in range(n):
                if nums[i] != 0:
                    l.append(0)
                else:
                    l.append(total)
        return l


n = 2
arr = [1, 0]
ans = Solution().productExceptSelf(arr, n)
print(*ans)
