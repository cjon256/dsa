#  Category: algorithms
#  Level: Medium
#  Percent: 39.828133%
# pylint: enable=useless-suppression
# pylint: disable=invalid-name
# pylint: disable=missing-class-docstring, missing-function-docstring, missing-module-docstring
# flake8: noqa


#  You are given an array of non-overlapping intervals intervals where
# intervals[i] = [starti, endi] represent the start and the end of the ith
# interval and intervals is sorted in ascending order by starti. You are also
# given an interval newInterval = [start, end] that represents the start and end
# of another interval.
#
#  Insert newInterval into intervals such that intervals is still sorted in
# ascending order by starti and intervals still does not have any overlapping
# intervals (merge overlapping intervals if necessary).
#
#  Return intervals after the insertion.
#
#
#  Example 1:
#
#  Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
#  Output: [[1,5],[6,9]]
#
#
#  Example 2:
#
#  Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
#  Output: [[1,2],[3,10],[12,16]]
#  Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
#
#
#
#  Constraints:
#
#
#  	0 <= intervals.length <= 10⁴
#  	intervals[i].length == 2
#  	0 <= starti <= endi <= 10⁵
#  	intervals is sorted by starti in ascending order.
#  	newInterval.length == 2
#  	0 <= start <= end <= 10⁵
#


import unittest
from typing import List


#  start_marker
class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        result = []
        new_interval_start, new_interval_end = newInterval
        idx = 0
        # add any non-overlapping intervals before
        while idx < len(intervals):
            curr_end = intervals[idx][1]
            if new_interval_start <= curr_end:
                break
            curr = intervals[idx]
            result.append(curr)
            idx += 1

        # merge overlapping intervals
        while idx < len(intervals):
            curr_start, curr_end = intervals[idx]
            if new_interval_end < curr_start:
                break
            new_interval_start = min(new_interval_start, curr_start)
            new_interval_end = max(new_interval_end, curr_end)
            idx += 1
        # add the combination
        result.append([new_interval_start, new_interval_end])

        # add non-overlapping intervals after
        result.extend(intervals[idx:])
        return result
        #  end_marker

    def insert_messy2(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        result = []
        new_start, new_end = newInterval
        if not intervals or (
            new_start <= intervals[0][0] and new_end >= intervals[-1][1]
        ):
            return [newInterval]
        newInterval_not_added = True
        for curr_interval in intervals:
            curr_start, curr_end = curr_interval
            if new_end < curr_start:
                # new interval is before current interval
                if newInterval_not_added:
                    result.append([new_start, new_end])
                    newInterval_not_added = False
                result.append(curr_interval)
            elif new_start <= curr_end:
                # new interval overlaps with current
                new_start = min(new_start, curr_start)
                new_end = max(new_end, curr_end)
            else:
                # new interval is after current
                result.append(curr_interval)
        if newInterval_not_added:
            # new interval is final
            result.append([new_start, new_end])
        return result

    def insert_messy(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        new_start, new_end = newInterval
        for curr, (curr_start, curr_end) in enumerate(intervals):
            if new_end < curr_start:
                # new interval is before current interval
                intervals.insert(curr, [new_start, new_end])
                return intervals
            if new_start <= curr_end:
                # new interval overlaps with current
                # but does it overlap with next?
                additions = 0
                for added_start, _ in intervals[curr + 1 :]:
                    if added_start > new_end:
                        break
                    additions += 1
                if additions == 0:
                    # no overlap with other intervals
                    intervals[curr] = [
                        min(curr_start, new_start),
                        max(curr_end, new_end),
                    ]
                    return intervals
                # overlap with other intervals
                new_start = min(new_start, curr_start)
                new_end = max(new_end, intervals[curr + additions][1])
                intervals[curr : curr + additions + 1] = [[new_start, new_end]]
                return intervals
        # new interval is after all current intervals
        intervals.append(newInterval)
        return intervals


class TestSolution(unittest.TestCase):
    def test_case_1(self):
        # new interval overlaps at end of one current interval
        intervals = [[1, 3], [6, 9]]
        newInterval = [2, 5]
        output = [[1, 5], [6, 9]]
        self.assertEqual(Solution().insert(intervals, newInterval), output)

    def test_case_2(self):
        # new interval overlaps with two current intervals
        intervals = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
        newInterval = [4, 8]
        output = [[1, 2], [3, 10], [12, 16]]
        self.assertEqual(Solution().insert(intervals, newInterval), output)

    def test_case_3(self):
        # new interval is after all current intervals
        intervals = [[1, 2], [3, 4]]
        newInterval = [5, 7]
        output = [[1, 2], [3, 4], [5, 7]]
        self.assertEqual(Solution().insert(intervals, newInterval), output)

    def test_case_4(self):
        # new interval is before all current intervals
        intervals = [[5, 7], [8, 10]]
        newInterval = [1, 2]
        output = [[1, 2], [5, 7], [8, 10]]
        self.assertEqual(Solution().insert(intervals, newInterval), output)

    def test_case_5(self):
        # new interval is before and overlaps with all current intervals
        intervals = [[1, 2], [3, 4], [5, 7], [8, 10]]
        newInterval = [1, 11]
        output = [[1, 11]]
        self.assertEqual(Solution().insert(intervals, newInterval), output)

    def test_case_6(self):
        # new interval is before and overlaps with all current intervals
        intervals = [[2, 3], [4, 5], [6, 7], [8, 9]]
        newInterval = [1, 11]
        output = [[1, 11]]
        self.assertEqual(Solution().insert(intervals, newInterval), output)

    def test_case_7(self):
        # new interval is only interval
        intervals = []
        newInterval = [0, 9]
        output = [[0, 9]]
        self.assertEqual(Solution().insert(intervals, newInterval), output)


if __name__ == "__main__":
    unittest.main()
