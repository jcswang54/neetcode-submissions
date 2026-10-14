class Solution:

    def encode(self, strs: List[str]) -> str:
        result = []
        for item in strs:
            length = len(item)
            result.append(str(length))
            result.append("#")
            result.append(item)
        return "".join(result)


    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':                   # move j to the '#'
                j += 1
            leng = int(s[i:j])                   # the digits are s[i..j-1]
            result.append(s[j+1 : j+1+leng])     # the word follows the '#'
            i = j + 1 + leng                     # jump to the next length
        return result