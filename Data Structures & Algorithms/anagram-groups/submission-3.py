class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """result = []

        for word in strs:
            placed = False
            for group in result:
                if sorted(group[0]) == sorted(word):
                    group.append(word)
                    placed = True
                    break
            if not placed:
                result.append([word])

        return result"""

        groups = {}
        for word in strs:
            key = "".join(sorted(word))
            if key in groups:
                groups[key].append(word)
            else:
                groups[key] =[word]
        return list(groups.values())

"""
        groups = {}                        # sorted word -> list of words
        for word in strs:
            key = "".join(sorted(word))    # "pots", "tops", "stop" all give "opst"
            if key not in groups:
                groups[key] = []
            groups[key].append(word)
        return list(groups.values())"""