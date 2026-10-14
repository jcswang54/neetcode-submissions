class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        rep = {}                    
        for num, count in freq.items():
            if count not in rep:
                rep[count] = []
            rep[count].append(num)

        result = []
        for count in sorted(rep.keys(), reverse=True):   # highest frequency first
            result.extend(rep[count])
            if len(result) >= k:
                break
        return result[:k]


        """
        for num in nums:
            freq[num] = freq.get(num,0) + 1
        for K,V in freq.items():
            rep[V] = K
        L = sorted(rep.keys(),reverse=True)
        return [rep[L[i]] for i in range(k)]
"""