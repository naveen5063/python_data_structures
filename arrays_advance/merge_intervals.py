# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    # @param intervals, a list of Intervals
    # @return a list of Interval
    def merge(self, intervals):
        initial_interval = intervals[0]
        out = self.get_intervals(intervals, initial_interval)
        return out

    def get_intervals(self, intervals, initial_interval):
        ans = []
        for i in range(1, len(intervals)):
            Interval(intervals[i])
            if intervals[i].end < initial_interval.start:
                ans.append(intervals[i])
            elif initial_interval.end < intervals[i].start:
                ans.append(initial_interval)
                for j in range(i, len(intervals)):
                    ans.append(intervals[j])
                return ans
            else:
                initial_interval.start = min(intervals[i].start, initial_interval.start)
                initial_interval.end = max(intervals[i].end, initial_interval.end)
        ans.append(initial_interval)
        return ans

#A = Interval([(1, 3), (2, 6), (8, 10), (15, 18)])
#A = Interval([1,3],[2,6],[8,10],[15,18])
#A = [ (1, 10), (2, 9), (3, 8), (4, 7), (5, 6), (6, 6) ]
#[1, 6], [8, 10], [15, 18]
A = [ (54, 75), (56, 60), (61, 86), (22, 43), (56, 87), (32, 53), (14, 81), (64, 65), (9, 42), (12, 33), (22, 58), (84, 90), (27, 59), (41, 48), (43, 47), (22, 29), (16, 23), (41, 72), (15, 87), (20, 59), (45, 84), (14, 77), (72, 93), (20, 58), (47, 53), (25, 88), (5, 89), (34, 97), (14, 47) ]

# A = Interval(1, 10)
# A = Interval(2, 9)
# A = Interval(3, 8)

s = Solution()
print(s.merge(A))