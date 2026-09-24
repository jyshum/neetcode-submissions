class Solution:

    def encode(self, strs: List[str]) -> str:
        e_output = ""
        for word in strs:
            e_output += str(len(word)) + "#" + word 
            # ex 5#hello
        return e_output

    def decode(self, s: str) -> List[str]:
        d_output = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            word = s[j+1:j+1+length]
            d_output.append(word)
            i = j+1+length
        return d_output


