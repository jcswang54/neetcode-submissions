class Solution:
    def isPalindrome(self, s: str) -> bool:
        st = "".join(c.lower() for c in s if c.isalnum())

        for i in range(len(st)):
            if st[i] != st[len(st)-i-1]:
                return False
        return True