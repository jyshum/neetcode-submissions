class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = ""
        for char in s:
            if char.isalnum():
                cleaned += char
        cleaned = cleaned.lower()

        if cleaned == cleaned[::-1]:
            return True
        else:
            return False


        