class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []

        prefix = []
        track = 1
        i = 0
        while i < len(nums):
            prefix.append(track)
            track *= nums[i]
            i += 1

        suffix = []
        track = 1
        i = len(nums)-1
        while i >= 0:
            suffix.append(track)
            track *= nums[i]
            i -= 1
        suffix.reverse()

        i = 0
        while i < len(nums):
            output.append(prefix[i]*suffix[i])
            i += 1

        return output

