class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # loop through each value in the array nums, and look up in a hashset containing all the elements in nums,  to see if there is a value that is +1 than the current value in the loop
        # if there is, then add 1 to the track and change the value in the loop to the value we just found and repeat the process for that new value (while loop or for loop???...)
        if len(nums) == 0:
            return 0
        
        cTrack = [] # keep track of all the consecutive amounts
        savedSet = set(nums) # put all elements into a hashset so we can instantly look up for the next consecutive
        longest = 0
        for num in savedSet:
            if num-1 not in savedSet:
                track = 1
                while num+track in savedSet:
                    track += 1
                longest = max(longest, track)
        
        return longest





        