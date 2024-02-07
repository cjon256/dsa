#  Category: algorithms
#  Level: Medium
#  Percent: 43.47565%
# pylint: enable=useless-suppression
# pylint: disable=invalid-name, line-too-long, too-few-public-methods
# pylint: disable=missing-class-docstring, missing-function-docstring, missing-module-docstring


#  You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.
#
#  Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.
#
#  You may assume that you have an infinite number of each kind of coin.
#
#
#  Example 1:
#
#  Input: coins = [1,2,5], amount = 11
#  Output: 3
#  Explanation: 11 = 5 + 5 + 1
#
#
#  Example 2:
#
#  Input: coins = [2], amount = 3
#  Output: -1
#
#
#  Example 3:
#
#  Input: coins = [1], amount = 0
#  Output: 0
#
#
#
#  Constraints:
#
#
#  	1 <= coins.length <= 12
#  	1 <= coins[i] <= 2³¹ - 1
#  	0 <= amount <= 10⁴
#

import unittest
from functools import lru_cache
from typing import List


def pretty_print_table(table):
    print("table: {")
    new_line = 0
    for key, value in sorted(table.items()):
        print(f"  {key: 4d}: {value: 10}, ", end="")
        new_line += 1
        if new_line % 5 == 0:
            print()
    print("}")


#  start_marker
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        if not coins:
            return -1
        MAX_AMOUNT = 2**32
        table = [MAX_AMOUNT] * (amount + 1)
        table[0] = 0
        for coin in coins:
            # print(f"coin: {coin}")
            for val in range(coin, amount + 1):
                table[val] = min(table[val], table[val - coin] + 1)
            # pretty_print_table(table)
        if table[amount] == MAX_AMOUNT:
            return -1
        return table[amount]

    #  end_marker
    def coinChange_recur(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        if not coins:
            return -1

        MAX_AMOUNT = 2**32
        solution_found = False

        @lru_cache(maxsize=None)
        def recursive_coin_change(amount: int) -> int:
            nonlocal coins, solution_found
            if amount < 0:
                return -1
            if amount == 0:
                solution_found = True
                return 0
            if amount > 0:
                min_coins = MAX_AMOUNT
                for coin in coins:
                    result = recursive_coin_change(amount - coin)
                    if result != -1:
                        min_coins = min(min_coins, result + 1)
                return min_coins
            return -1

        coins.sort(reverse=True)
        answer = recursive_coin_change(amount)
        if solution_found:
            return answer
        return -1


class TestSolution(unittest.TestCase):
    def test_case_1(self):
        coins = [1, 2, 5]
        amount = 11
        expected_result = 3
        self.assertEqual(Solution().coinChange(coins, amount), expected_result)

    def test_case_2(self):
        coins = [2]
        amount = 3
        expected_result = -1
        self.assertEqual(Solution().coinChange(coins, amount), expected_result)

    def test_case_3(self):
        coins = [1]
        amount = 0
        expected_result = 0
        self.assertEqual(Solution().coinChange(coins, amount), expected_result)

    def test_case_4(self):
        coins = [1, 15, 25]
        amount = 30
        expected_result = 2
        self.assertEqual(Solution().coinChange(coins, amount), expected_result)

    def test_case_5(self):
        coins = [1, 5, 25, 16]
        amount = 48
        expected_result = 3
        self.assertEqual(Solution().coinChange(coins, amount), expected_result)

    def test_case_6(self):
        coins = [3, 5]
        amount = 6
        expected_result = 2
        self.assertEqual(Solution().coinChange(coins, amount), expected_result)

    def test_case_7(self):
        coins = []
        amount = 100
        expected_result = -1
        self.assertEqual(Solution().coinChange(coins, amount), expected_result)

    def test_case_8(self):
        coins = []
        amount = 0
        expected_result = 0
        self.assertEqual(Solution().coinChange(coins, amount), expected_result)

    def test_case_9(self):
        coins = [1, 2, 5, 93]
        amount = 1003
        expected_result = 26
        self.assertEqual(Solution().coinChange(coins, amount), expected_result)


if __name__ == "__main__":
    unittest.main()
    # coins = [1, 5, 25, 16]
    # amount = 48
    # print(Solution().coinChange(coins, amount))
    # print("-------")
    # coins = [5, 7, 9]
    # amount = 210
    # print(Solution().coinChange(coins, amount))
