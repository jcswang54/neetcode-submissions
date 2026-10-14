class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
        
        ###class Solution:
    """
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        l = list(s)
        for letter in t:
            if letter not in l:
                return False
            l.remove(letter)

        return len(l) == 0

        this code is too slow
        """
        