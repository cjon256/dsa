#  Category: algorithms
#  Level: Easy
#  Percent: 57.80254%
import unittest
from typing import List

#  Given an array of meeting time intervals where intervals[i] = [starti, endi], determine if a person could attend all meetings.
#
#
#  Example 1:
#  Input: intervals = [[0,30],[5,10],[15,20]]
#  Output: false
#  Example 2:
#  Input: intervals = [[7,10],[2,4]]
#  Output: true
#
#
#  Constraints:
#
#
#  	0 <= intervals.length <= 10⁴
#  	intervals[i].length == 2
#  	0 <= starti < endi <= 10⁶
#


#  start_marker
class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        sort_intervals = sorted(intervals, key=lambda x: x[0])
        last_end = 0
        for i, (start, end) in enumerate(sort_intervals):
            if start < last_end:
                return False
            last_end = end
        return True


#  end_marker


class TestSolution(unittest.TestCase):
    def test_0(self):
        intervals = [[0, 30], [5, 10], [15, 20]]
        res = False
        self.assertEqual(res, Solution().canAttendMeetings(intervals))

    def test_1(self):
        intervals = [[7, 10], [2, 4]]
        res = True
        self.assertEqual(res, Solution().canAttendMeetings(intervals))


if __name__ == "__main__":
    unittest.main()
