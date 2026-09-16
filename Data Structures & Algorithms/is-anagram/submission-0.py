class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # check for duplicates between s & t
        # keep track of duplicate count and see if those match
        if len(s) != len(t):
            return False

        lettersS = {}
        for letterS in s:
            if letterS in lettersS:
                lettersS[letterS] += 1
            else:
                lettersS[letterS] = 1

        lettersT = {}
        for letterT in t:
            if letterT in lettersT:
                lettersT[letterT] += 1
            else:
                lettersT[letterT] = 1

        for checkforDup in lettersS:
            if checkforDup not in lettersT:
                return False
            if lettersS[checkforDup] != lettersT[checkforDup]:
                return False
        
        return True

        
        

        


        

        

        

    
            



                    

