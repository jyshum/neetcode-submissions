class Solution:
    def search(self, nums: List[int], target: int) -> int:
        top = len(nums)
        bottom = 0

        while top > bottom:
            middle = (top+bottom)//2
            if target == nums[middle]:
                return middle
            elif target < nums[middle]:
                top = middle
            else:
                bottom = middle+1

        return -1