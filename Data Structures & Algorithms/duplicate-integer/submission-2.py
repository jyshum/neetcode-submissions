class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seenList = set()

        for value in nums:
            if value in seenList:
                return True
            seenList.add(value)

        return False