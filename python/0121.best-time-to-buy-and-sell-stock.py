#  Category: algorithms
#  Level: Easy
#  Percent: 53.488167%


#  You are given an array prices where prices[i] is the price of a given stock on the ith day.
#
#  You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
#
#  Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
#
#
#  Example 1:
#
#  Input: prices = [7,1,5,3,6,4]
#  Output: 5
#  Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
#  Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
#
#
#  Example 2:
#
#  Input: prices = [7,6,4,3,1]
#  Output: 0
#  Explanation: In this case, no transactions are done and the max profit = 0.
#
#
#
#  Constraints:
#
#
#  	1 <= prices.length <= 10⁵
#  	0 <= prices[i] <= 10⁴
#
import unittest
from typing import List


#  start_marker
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


#  end_marker
class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_case_1(self):
        self.assertEqual(self.solution.maxProfit([7, 1, 5, 3, 6, 4]), 5)

    def test_case_2(self):
        self.assertEqual(self.solution.maxProfit([7, 6, 4, 3, 1]), 0)

    def test_case_3(self):
        self.assertEqual(self.solution.maxProfit([7, 2, 9, 1, 5, 7]), 7)


if __name__ == "__main__":
    unittest.main()
