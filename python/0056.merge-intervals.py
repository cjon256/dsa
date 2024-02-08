#  Category: algorithms
#  Level: Medium
#  Percent: 46.933205%
# pylint: enable=useless-suppression
# pylint: disable=invalid-name, line-too-long, too-few-public-methods
# pylint: disable=missing-class-docstring, missing-function-docstring, missing-module-docstring


#  Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.
#
#
#  Example 1:
#
#  Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
#  Output: [[1,6],[8,10],[15,18]]
#  Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
#
#
#  Example 2:
#
#  Input: intervals = [[1,4],[4,5]]
#  Output: [[1,5]]
#  Explanation: Intervals [1,4] and [4,5] are considered overlapping.
#
#
#
#  Constraints:
#
#
#  	1 <= intervals.length <= 10⁴
#  	intervals[i].length == 2
#  	0 <= starti <= endi <= 10⁴
#

import unittest
from typing import Dict, List, Optional


#  start_marker
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        max_num = 0
        for _, e in intervals:
            max_num = max(max_num, e)
        interval_arr = [0] * (max_num + 1)
        for s, e in intervals:
            if s == e:
                interval_arr[s] |= 8
            else:
                interval_arr[s] |= 4
                for i in range(s + 1, e):
                    interval_arr[i] |= 1
                interval_arr[e] |= 2
        result: List[List[int]] = []
        st = -1
        for i, v in enumerate(interval_arr):
            match v:
                case 2 | 10:
                    result.append([st, i])
                    st = -1
                case 4 | 12:
                    st = i
                case 8:
                    result.append([i, i])
                case _:
                    pass
        return result

    #  end_marker
    def merge_messy(self, intervals: List[List[int]]) -> List[List[int]]:
        interval_dict: Dict[int, str] = {}
        for s, e in intervals:
            if s == e:
                if interval_dict.get(s) is None:
                    interval_dict[s] = "point"
                continue
            match interval_dict.get(s, "start"):
                case "in" | "end":
                    interval_dict[s] = "in"
                case _:
                    interval_dict[s] = "start"
            for i in range(s + 1, e):
                interval_dict[i] = "in"
            match interval_dict.get(e, "end"):
                case "start" | "in":
                    interval_dict[e] = "in"
                case _:
                    interval_dict[e] = "end"
        nums = sorted(interval_dict.keys())
        result: List[List[int]] = []
        current: Optional[int] = None
        for i in nums:
            if interval_dict[i] == "point":
                result.append([i, i])
            elif interval_dict[i] == "start":
                current = i
            elif interval_dict[i] == "end":
                if current is not None:
                    result.append([current, i])
                current = None
        return result

    #  end_marker
    def merge_vanilla(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        result = []
        prev = intervals[0]
        for inter in intervals[1:]:
            if prev[1] < inter[0]:
                result.append(prev)
                prev = inter
            else:
                prev = [min(prev[0], inter[0]), max(prev[1], inter[1])]
        result.append(prev)
        return result


#  end_marker
class TestSolution(unittest.TestCase):
    def test_case_1(self):
        intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
        expected_result = [[1, 6], [8, 10], [15, 18]]
        result = Solution().merge(intervals)
        self.assertEqual(result, expected_result)

    def test_case_2(self):
        intervals = [[1, 4], [4, 5]]
        expected_result = [[1, 5]]
        result = Solution().merge(intervals)
        self.assertEqual(result, expected_result)

    def test_case_3(self):
        intervals = [[1, 4], [0, 4]]
        expected_result = [[0, 4]]
        result = Solution().merge(intervals)
        self.assertEqual(result, expected_result)

    def test_case_4(self):
        intervals = [[1, 4], [0, 0]]
        expected_result = [[0, 0], [1, 4]]
        result = Solution().merge(intervals)
        self.assertEqual(result, expected_result)

    def test_case_5(self):
        intervals = [[1, 4], [0, 1]]
        expected_result = [[0, 4]]
        result = Solution().merge(intervals)
        self.assertEqual(result, expected_result)

    def test_case_6(self):
        intervals = [[1, 4], [2, 3]]
        expected_result = [[1, 4]]
        result = Solution().merge(intervals)
        self.assertEqual(result, expected_result)

    def test_case_7(self):
        intervals = [[1, 4], [0, 5]]
        expected_result = [[0, 5]]
        result = Solution().merge(intervals)
        self.assertEqual(result, expected_result)

    def test_case_8(self):
        intervals = [[1, 4], [0, 0], [2, 7]]
        expected_result = [[0, 0], [1, 7]]
        result = Solution().merge(intervals)
        self.assertEqual(result, expected_result)

    def test_case_9(self):
        intervals = [[1, 4], [0, 0], [0, 3]]
        expected_result = [[0, 4]]
        result = Solution().merge(intervals)
        self.assertEqual(result, expected_result)

    def test_case_10(self):
        intervals = [[2, 3], [5, 5], [2, 2], [3, 4], [3, 4]]
        expected_result = [[2, 4], [5, 5]]
        result = Solution().merge(intervals)
        self.assertEqual(result, expected_result)

    def test_case_11(self):
        intervals = [[1, 4], [1, 1], [0, 1]]
        expected_result = [[0, 4]]
        result = Solution().merge(intervals)
        self.assertEqual(result, expected_result)

    def test_case_12(self):
        intervals = [[1, 4], [4, 4], [0, 1]]
        expected_result = [[0, 4]]
        result = Solution().merge(intervals)
        self.assertEqual(result, expected_result)


if __name__ == "__main__":
    unittest.main()
