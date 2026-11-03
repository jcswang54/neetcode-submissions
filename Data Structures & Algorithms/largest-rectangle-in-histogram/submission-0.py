class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        hs = heights + [0]     # sentinel: a height-0 bar at the end flushes the stack
        stack = []                   # indices; heights increasing from bottom to top
        best = 0
        for i, h in enumerate(hs):
            while stack and hs[stack[-1]] > h:
                height = hs[stack.pop()]               # this bar's rectangle ends here
                left = stack[-1] if stack else -1      # nearest shorter bar on the left
                best = max(best, height * (i - left - 1))
            stack.append(i)
        return best