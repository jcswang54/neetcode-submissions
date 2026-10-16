class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0 # left bar position
        r =len(heights)-1
        best  = 0 
        best_pair = (0,0)

        while l<r:
            area = (r-l) *min(heights[l], heights[r])
            if area > best:
                best_pair = (l,r)
                best = area
            if heights[l]< heights[r]:
                l += 1
            else:
                r -=1
        return best

"""
        area  = (rpos-lpos)* min(heights[lpos], heights[rpos])

        while lpos < rpos:
            if heights[lpos]< heights[lpos+1]:
                cand_area = (rpos- lpos - 1) *min(heights[lpos+1],heights[rpos])
                if cand_area> area:
                    area = cand_area
                    lpos +=1

            if heights[rpos]< heights[rpos-1]:
                cand_area = (rpos- lpos - 1) *min(heights[lpos],heights[rpos-1])
                if cand_area > area:
                    area = cand_area
                    rpos -=1
            break
              
        return area
"""