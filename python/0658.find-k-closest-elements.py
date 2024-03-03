#  Category: algorithms
#  Level: Medium
#  Percent: 47.21237%
# pylint: enable=useless-suppression
# pylint: disable=invalid-name, line-too-long, too-few-public-methods
# pylint: disable=missing-class-docstring, missing-function-docstring, missing-module-docstring


#  Given a sorted integer array arr, two integers k and x, return the k closest integers to x in the array. The result should also be sorted in ascending order.
#
#  An integer a is closer to x than an integer b if:
#
#
#  	|a - x| < |b - x|, or
#  	|a - x| == |b - x| and a < b
#
#
#
#  Example 1:
#  Input: arr = [1,2,3,4,5], k = 4, x = 3
#  Output: [1,2,3,4]
#  Example 2:
#  Input: arr = [1,2,3,4,5], k = 4, x = -1
#  Output: [1,2,3,4]
#
#
#  Constraints:
#
#
#  	1 <= k <= arr.length
#  	1 <= arr.length <= 10⁴
#  	arr is sorted in ascending order.
#  	-10⁴ <= arr[i], x <= 10⁴
#


import heapq
import unittest
from typing import List


#  start_marker
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        diffs = []
        for i in range(len(arr)):
            diffs.append(abs(arr[i] - x))
        total_diff = 0
        end = min(range(len(diffs)), key=diffs.__getitem__)
        start = max(end - k, 0)
        while end < len(arr) and end < k:
            total_diff += diffs[end]
            end += 1
        while end < len(arr):
            if diffs[end] < diffs[start]:
                total_diff += diffs[end] - diffs[start]
                start += 1
                end += 1
            else:
                break
        return arr[start:end]
        #  end_marker


from dataclasses import dataclass


@dataclass
class DistVal:
    dist: int
    val: int

    def __lt__(self, other):
        if self.dist == other.dist:
            return self.val > other.val
        return self.dist > other.dist


class SolutionHeap:
    def findClosestElements_heap(self, arr: List[int], k: int, x: int) -> List[int]:
        def closeness(n: int) -> DistVal:
            return DistVal(dist=abs(n - x), val=n)

        h: List[DistVal] = []
        for _ in range(k):
            dv = closeness(arr.pop())
            heapq.heappush(h, dv)
        while arr:
            dv = closeness(arr.pop())
            if dv.dist == h[0].dist or dv > h[0]:
                heapq.heappushpop(h, dv)
        return sorted([d.val for d in h])


class TestSolution(unittest.TestCase):
    def test_case_1(self):
        arr = [1, 2, 3, 4, 5]
        k = 4
        x = 3
        expected = [1, 2, 3, 4]
        result = Solution().findClosestElements(arr, k, x)
        self.assertEqual(sorted(result), expected)

    def test_case_2(self):
        arr = [1, 2, 3, 4, 5]
        k = 4
        x = -1
        expected = [1, 2, 3, 4]
        result = Solution().findClosestElements(arr, k, x)
        self.assertEqual(sorted(result), expected)

    def test_case_3(self):
        arr = [1, 2, 3, 4, 5]
        k = 4
        x = 5
        expected = [2, 3, 4, 5]
        result = Solution().findClosestElements(arr, k, x)
        self.assertEqual(sorted(result), expected)

    def test_case_4(self):
        arr = [1, 2, 3, 4, 5]
        k = 4
        x = 13
        expected = [2, 3, 4, 5]
        result = Solution().findClosestElements(arr, k, x)
        self.assertEqual(sorted(result), expected)

    def test_case_5(self):
        arr = [1, 1, 1, 10, 10, 10]
        k = 1
        x = 9
        expected = [10]
        result = Solution().findClosestElements(arr, k, x)
        self.assertEqual(sorted(result), expected)

    def test_case_6(self):
        arr = [1, 1, 1, 10, 10, 10]
        k = 1
        x = 0
        expected = [1]
        result = Solution().findClosestElements(arr, k, x)
        self.assertEqual(sorted(result), expected)

    def test_case_7(self):
        arr = [1, 1, 1, 10, 10, 10]
        k = 1
        x = 1
        expected = [1]
        result = Solution().findClosestElements(arr, k, x)
        self.assertEqual(sorted(result), expected)

    def test_case_8(self):
        arr = [1, 1, 1, 10, 10, 10]
        k = 1
        x = 2
        expected = [1]
        result = Solution().findClosestElements(arr, k, x)
        self.assertEqual(sorted(result), expected)

    def test_case_9(self):
        arr = [1, 1, 1, 10, 10, 10]
        k = 1
        x = 3
        expected = [1]
        result = Solution().findClosestElements(arr, k, x)
        self.assertEqual(sorted(result), expected)

    def test_case_10(self):
        arr = [1, 1, 1, 10, 10, 10]
        k = 1
        x = 4
        expected = [1]
        result = Solution().findClosestElements(arr, k, x)
        self.assertEqual(sorted(result), expected)

    def test_case_11(self):
        arr = [1, 1, 1, 10, 10, 10]
        k = 1
        x = 5
        expected = [1]
        result = Solution().findClosestElements(arr, k, x)
        self.assertEqual(sorted(result), expected)

    def test_case_12(self):
        arr = [1, 1, 1, 10, 10, 10]
        k = 1
        x = 6
        expected = [10]
        result = Solution().findClosestElements(arr, k, x)
        self.assertEqual(sorted(result), expected)


if __name__ == "__main__":
    unittest.main()
