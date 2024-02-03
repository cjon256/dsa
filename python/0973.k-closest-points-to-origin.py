#  Category: algorithms
#  Level: Medium
#  Percent: 66.08213%
# pylint: enable=useless-suppression
# pylint: disable=invalid-name, too-few-public-methods
# pylint: disable=missing-class-docstring, missing-function-docstring, missing-module-docstring


#  Given an array of points where points[i] = [xi, yi] represents a point on
#  the X-Y plane and an integer k, return the k closest points to the origin
#  (0, 0).
#
#  The distance between two points on the X-Y plane is the Euclidean distance
#  (i.e., √(x₁ - x₂)² + (y₁ - y₂)²).
#
#  You may return the answer in any order. The answer is guaranteed to be
#  unique (except for the order that it is in).
#
#
#  Example 1:
#
#  Input: points = [[1,3],[-2,2]], k = 1
#  Output: [[-2,2]]
#  Explanation:
#  The distance between (1, 3) and the origin is sqrt(10).
#  The distance between (-2, 2) and the origin is sqrt(8).
#  Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
#  We only want the closest k = 1 points from the origin, so the answer is just [[-2,2]].
#
#
#  Example 2:
#
#  Input: points = [[3,3],[5,-1],[-2,4]], k = 2
#  Output: [[3,3],[-2,4]]
#  Explanation: The answer [[-2,4],[3,3]] would also be accepted.
#
#
#
#  Constraints:
#
#
#  	1 <= k <= points.length <= 10⁴
#  	-10⁴ <= xi, yi <= 10⁴
#

import unittest
from typing import List


#  start_marker
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def distance_from_origin_squared(point: List[int]) -> int:
            return point[0] ** 2 + point[1] ** 2

        return sorted(points, key=distance_from_origin_squared)[:k]
        #  end_marker


class TestSolution(unittest.TestCase):
    def test_case_1(self):
        points = [[1, 3], [-2, 2]]
        k = 1
        expected_result = [[-2, 2]]
        self.assertEqual(Solution().kClosest(points, k), expected_result)

    def test_case_2(self):
        points = [[3, 3], [5, -1], [-2, 4]]
        k = 2
        expected_result = [[3, 3], [-2, 4]]
        self.assertEqual(Solution().kClosest(points, k), expected_result)


if __name__ == "__main__":
    unittest.main()
