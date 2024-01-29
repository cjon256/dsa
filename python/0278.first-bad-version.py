#  Category: algorithms
#  Level: Easy
#  Percent: 44.09307%


#  You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.
#
#  Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.
#
#  You are given an API bool isBadVersion(version) which returns whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.
#
#
#  Example 1:
#
#  Input: n = 5, bad = 4
#  Output: 4
#  Explanation:
#  call isBadVersion(3) -> false
#  call isBadVersion(5) -> true
#  call isBadVersion(4) -> true
#  Then 4 is the first bad version.
#
#
#  Example 2:
#
#  Input: n = 1, bad = 1
#  Output: 1
#
#
#
#  Constraints:
#
#
#  	1 <= bad <= n <= 2³¹ - 1
#
# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:


import unittest
from typing import Callable

#  start_marker


class Solution:
    def firstBadVersion(self, n: int, isBadVersion: Callable[[int], bool]) -> int:
        highest_good = 0
        lowest_bad = n + 1
        curr = n // 2
        while (lowest_bad - highest_good) > 1:
            if isBadVersion(curr):
                lowest_bad = curr
                curr = (highest_good + curr + 1) // 2
            else:
                highest_good = curr
                curr = (curr + lowest_bad) // 2
        return lowest_bad


#  end_marker
def generate_isBadVersion(first_bad: int) -> Callable[[int], bool]:
    def isBadVersion(version: int) -> bool:
        return version >= first_bad

    return isBadVersion


class Test(unittest.TestCase):
    def test_one(self):
        isBadVersion = generate_isBadVersion(4)
        self.assertEqual(Solution().firstBadVersion(5, isBadVersion), 4)

    def test_two(self):
        isBadVersion = generate_isBadVersion(1)
        self.assertEqual(Solution().firstBadVersion(1, isBadVersion), 1)


if __name__ == "__main__":
    unittest.main()
