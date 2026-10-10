class Solution:
    def findMin(self, nums: List[int]) -> int:
        # this array there are two sorted arrays
        # comparing two numbers (middle is fastest) with the top shows where the two sorted arrays are
        # the first element in both "arrays" will not be the same 
        # every number in the first array should be bigger than every number in the second array
                    # this dosent apply though if it was fully rotated
        
        top = len(nums)-1
        bottom = 0

        while top > bottom:
            middle = (top+bottom) // 2

            if nums[middle] > nums[top]: # the smallest number has to be in the right side (middle+1 to top)
                bottom = middle + 1 # setting the new half, 
            elif nums[middle] < nums[top]: # the numbers before middle should be smaller, (bottom to middle)
                top = middle # setting the new half

        return nums[bottom] # return the value of bottom




        
