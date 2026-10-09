class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = {} # set up counts of letters
        best = 0 # best substring length

        left = 0 # starting from left point
        for right in range(len(s)):
            letter = s[right]
            counts[letter] = counts.get(letter, 0) + 1 # adding count to a letter

            mostCommon = max(counts.values()) # getting the max count in each window
            size = right-left+1 # amount of letters in the current window
            needed = size - mostCommon # needed replacements XYY 3 - 2 = 1, X is the replacement

            while needed > k:
                counts[s[left]] -= 1 # take away 1 count of left character from dict to shift window left
                left += 1 # start checking the next window, shifted one character to the right
                mostCommon = max(counts.values()) # updating most common 
                size = right-left+1 # update anount of letters in current winodw
                needed = size - mostCommon # update needed replacements
            
            best = max(best, size)

        return best

        