import unittest
from typing import List
from collections import Counter


class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        try:
            return Counter(arr).most_common(1)[0][0]
        except IndexError:
            return None


class TestSolution(unittest.TestCase):
    def test1(self):
        self.assertEqual(Solution().findSpecialInteger(
            [1, 2, 2, 6, 6, 6, 6, 7, 10]), 6)

    def test2(self):
        self.assertEqual(Solution().findSpecialInteger([1, 1]), 1)

    def test3(self):
        self.assertEqual(Solution().findSpecialInteger([]), None)

    def test4(self):
        self.assertEqual(Solution().findSpecialInteger(
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]), 1)


if __name__ == '__main__':
    unittest.main()
