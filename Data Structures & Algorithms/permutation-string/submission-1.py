class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        se = sorted(s1)

        for i in range(len(s2)):
            if se == sorted(s2[i:i+n]):
                return True
        return False

