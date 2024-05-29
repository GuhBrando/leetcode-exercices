class Solution:
    def twoSum(self, nums, target: int):
        """
            - Collect variables to sum and return the first and secound indice without repeting them self
            - Return list of both index
        """
        first_number = 0
        secound_number = 0
        while True:
            for i in range(0, len(nums)):
                if first_number == secound_number:
                    secound_number += 1
                    continue
                if nums[first_number] + nums[secound_number] == target:
                    return [first_number, secound_number]
                secound_number += 1

            secound_number = 0
            first_number += 1
        return [first_number, secound_number]
    
Solution().twoSum([3,2,4], 6)