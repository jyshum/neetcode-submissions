class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # loop through strs to look for anagrams, if you find a pair of anagrams, 
        # move them into a list inside a list. (nested list), if not, move the current 
        # word into the sublist as just one string

        # anagram check function to loop through strs in O(n) AND to store the indicies 
        # of these the pair of strings that are anagrams and then add strs[i] strs[j] 
        # into a sublist, order dosent matter in sublist so u can just add it in. 
        # initialize output sublist as output
        #                           USE output.append(strs[i], strs[j])
        # comparing each string to each other in the array as a sorted string using the .sort
        
        hashMap = {}
        for i, word in enumerate(strs):
            key = "".join(sorted(word))
            if key in hashMap:
                hashMap[key].append(word)
            else:
                hashMap[key] = [word]

        return list(hashMap.values())
            
            
        
        
