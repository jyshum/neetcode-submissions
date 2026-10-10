class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        top = len(nums)-1
        bottom = 0

        while top > bottom:
            middle = (top+bottom) // 2

            if nums[middle] > nums[top]: # middle cant be the samllest, smallest number must be after middle
                bottom = middle + 1
            elif nums[middle] < nums[top]:
                top = middle

        return nums[bottom]




        
