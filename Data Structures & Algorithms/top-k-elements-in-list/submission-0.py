class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # create a dict to keep track of number freq
        # {1:1, 2:2, 3:3}

        # method to return only k most freq numbers
        # [2,3]
        freq = {}
        for value in nums:
            if value in freq:
                freq[value] += 1
            else:
                freq[value] = 1.    # keeps track of numbers and their freq in a dict
        
        sorted_keys = sorted(freq, key=freq.get, reverse=True)
        return sorted_keys[:k]
            