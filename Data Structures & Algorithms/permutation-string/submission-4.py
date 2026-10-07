class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # sliding window problem
        # window should always have a length of len(s1)
        s1 = "".join(sorted(s1))

        i = 0    
        while i <= len(s2)-len(s1):
            substring = "".join(sorted(s2[i:i+len(s1)]))
            if substring == s1:
                return True
            i += 1

        return False
        
