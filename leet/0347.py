import unittest
from typing import List
from collections import Counter


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return [n for n, _ in Counter(nums).most_common(k)]


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_1(self):
        nums = [1, 1, 1, 2, 2, 3]
        k = 2
        expected = [1, 2]
        self.assertEqual(self.solution.topKFrequent(nums, k), expected)

    def test_2(self):
        nums = [1]
        k = 1
        expected = [1]
        self.assertEqual(self.solution.topKFrequent(nums, k), expected)


if __name__ == '__main__':
    unittest.main()
