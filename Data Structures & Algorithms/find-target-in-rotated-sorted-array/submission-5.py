class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # searching for the value of target
        # the array is sorted into two increasing arrays, first half elements are all larger than elements in second half, dosent apply if it became the same array (rotated the length)

        right = len(nums)-1
        left = 0

        while right >= left:
            middle =(right+left)//2

            if nums[middle] == target:
                return middle
            if nums[middle] >= nums[left]:
                if target > nums[middle] or target < nums[left]:
                    left = middle + 1
                else:
                    right = middle - 1
            else:
                if target < nums[middle] or target >= nums[left]:
                    right = middle - 1
                else:
                    left = middle + 1

        return -1
