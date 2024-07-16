class Solution:
    def countPairs(self, nums, target: int) -> int:
        combinations = 0
        i = 0
        j = 0

        for ix in nums:
            for jx in nums:
                if nums[i] + nums[j] < target and i < j:
                    print(i, j)
                    combinations += 1
                j += 1
            i += 1
            j = 0
            
        return combinations

Solution().countPairs([9,-5,-5,5,-5,-4,-6,6,-6], 3)