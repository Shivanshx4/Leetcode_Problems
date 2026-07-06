class Solution:
    def removeCoveredIntervals(self, intervals):
        intervals.sort(key=lambda x: (x[0], -x[1]))
        
        count = 0
        max_r = 0
        
        for _, r in intervals:
            if r > max_r:
                count += 1
                max_r = r
                
        return count