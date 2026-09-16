class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # outputting indices 
        # taking in values[i & j] and seeing if they add up to target

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]