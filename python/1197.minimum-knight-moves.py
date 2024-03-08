#  Category: algorithms
#  Level: Medium
#  Percent: 40.3%
# pylint: enable=useless-suppression
# pylint: disable=invalid-name, line-too-long, too-few-public-methods
# pylint: disable=missing-class-docstring, missing-function-docstring, missing-module-docstring

#
# In an infinite chess board with coordinates from -infinity to +infinity, you have a knight at square [0, 0].
#
# A knight has 8 possible moves it can make, as illustrated below. Each move is two squares in a cardinal direction, then one square in an orthogonal direction.
#
# Return the minimum number of steps needed to move the knight to the square [x, y]. It is guaranteed the answer exists.
#
#
#
# Example 1:
#
# Input: x = 2, y = 1
# Output: 1
# Explanation: [0, 0] → [2, 1]
#
# Example 2:
#
# Input: x = 5, y = 5
# Output: 4
# Explanation: [0, 0] → [2, 1] → [4, 2] → [3, 4] → [5, 5]
#
#
#
# Constraints:
#
#     -300 <= x, y <= 300
#     0 <= |x| + |y| <= 300
#

import unittest


#  start_marker
class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        pass

        #  end_marker


class TestSolution(unittest.TestCase):
    def test_case_1(self):
        pass


if __name__ == "__main__":
    unittest.main()
