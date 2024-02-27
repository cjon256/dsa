#  Category: algorithms
#  Level: Medium
#  Percent: 51.03485%
# pylint: enable=useless-suppression
# pylint: disable=invalid-name, line-too-long, too-few-public-methods
# pylint: disable=missing-class-docstring, missing-function-docstring, missing-module-docstring


#  Given an array of meeting time intervals intervals where intervals[i] = [starti, endi], return the minimum number of conference rooms required.
#
#
#  Example 1:
#  Input: intervals = [[0,30],[5,10],[15,20]]
#  Output: 2
#  Example 2:
#  Input: intervals = [[7,10],[2,4]]
#  Output: 1
#
#
#  Constraints:
#
#
#  	1 <= intervals.length <= 10⁴
#  	0 <= starti < endi <= 10⁶
#

import heapq
import unittest
from collections import defaultdict
from typing import Dict, List


#  start_marker
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        stop_heap: List[int] = []
        curr = max_meetings = 0
        while intervals:
            if stop_heap and intervals[0][0] >= stop_heap[0]:
                heapq.heappop(stop_heap)
                curr -= 1
            else:
                _, stop = intervals.pop(0)
                heapq.heappush(stop_heap, stop)
                curr += 1
            max_meetings = max(max_meetings, curr)
        return max_meetings
        #  end_marker

    def minMeetingRooms_dict(self, intervals: List[List[int]]) -> int:
        times: Dict[int, int] = defaultdict(lambda: 0)
        for start, stop in intervals:
            times[start] += 1
            times[stop] -= 1
        curr = max_meetings = 0
        for t in sorted(times):
            curr += times[t]
            max_meetings = max(max_meetings, curr)
        return max_meetings


class TestSolution(unittest.TestCase):
    def test_case_1(self):
        intervals = [[0, 30], [5, 10], [15, 20]]
        expected = 2
        result = Solution().minMeetingRooms(intervals)
        self.assertEqual(result, expected)

    def test_case_2(self):
        intervals = [[7, 10], [2, 4]]
        expected = 1
        result = Solution().minMeetingRooms(intervals)
        self.assertEqual(result, expected)

    def test_case_3(self):
        intervals = [[7, 10], [10, 11], [10, 14]]
        expected = 2
        result = Solution().minMeetingRooms_dict(intervals)
        self.assertEqual(result, expected)

    def test_case_4(self):
        intervals = []
        expected = 0
        result = Solution().minMeetingRooms_dict(intervals)
        self.assertEqual(result, expected)

    def test_case_5(self):
        intervals = [[1, 2], [2, 3], [3, 4], [4, 5]]
        expected = 1
        result = Solution().minMeetingRooms_dict(intervals)
        self.assertEqual(result, expected)

    def test_case_6(self):
        intervals = [[13, 15], [1, 13]]
        expected = 1
        result = Solution().minMeetingRooms_dict(intervals)
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
