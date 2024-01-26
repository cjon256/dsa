import unittest
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest_seen = None
        best_deal = 0
        for price in prices:
            if lowest_seen is None or price < lowest_seen:
                lowest_seen = price
            else:
                if price - lowest_seen > best_deal:
                    best_deal = price - lowest_seen
        return best_deal


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_case_1(self):
        self.assertEqual(self.solution.maxProfit([7, 1, 5, 3, 6, 4]), 5)

    def test_case_2(self):
        self.assertEqual(self.solution.maxProfit([7, 6, 4, 3, 1]), 0)

    def test_case_3(self):
        self.assertEqual(self.solution.maxProfit([7, 2, 9, 1, 5, 7]), 7)


if __name__ == '__main__':
    unittest.main()
