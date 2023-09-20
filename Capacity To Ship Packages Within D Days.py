class Solution:
    def leastWeightCapacity(self, arr, N, D):
        low = max(arr)
        high = sum(arr) + 1

        while low < high:
            mid = (high + low) // 2

            boatcapacity = mid
            boatcount = 1

            for package in arr:
                if package > boatcapacity:
                    boatcount += 1
                    boatcapacity = mid

                boatcapacity -= package

            if boatcount <= D:
                high = mid
            else:
                low = mid + 1

        return low


N = 12
arr = [17, 20, 2, 17, 10, 4, 20, 15, 1, 3, 9, 15]
D = 12
ob = Solution()
print(ob.leastWeightCapacity(arr, N, D))
