class Solution:
    def isPalindrome(self, s: str) -> bool:

        clean = ""
        
        for ch in s:
            if ch.isalnum():
                clean += ch.lower()
        character = clean[::-1]
        if clean == character:
            return True
        return False