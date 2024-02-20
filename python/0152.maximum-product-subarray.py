#  Category: algorithms
#  Level: Medium
#  Percent: 34.925198%
# pylint: enable=useless-suppression
# pylint: disable=invalid-name, line-too-long, too-few-public-methods
# pylint: disable=missing-class-docstring, missing-function-docstring, missing-module-docstring


#  Given an integer array nums, find a subarray that has the largest product, and return the product.
#
#  The test cases are generated so that the answer will fit in a 32-bit integer.
#
#
#  Example 1:
#
#  Input: nums = [2,3,-2,4]
#  Output: 6
#  Explanation: [2,3] has the largest product 6.
#
#
#  Example 2:
#
#  Input: nums = [-2,0,-1]
#  Output: 0
#  Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
#
#
#
#  Constraints:
#
#
#  	1 <= nums.length <= 2 * 10⁴
#  	-10 <= nums[i] <= 10
#  	The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
#


import unittest
from functools import reduce
from typing import List


#  start_marker
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        curr_max = 1
        curr_min = 1
        for n in nums:
            if n < 0:
                curr_max, curr_min = curr_min, curr_max
            curr_max = max(curr_max * n, n)
            curr_min = min(curr_min * n, n)
            res = max(res, curr_max)
        return res
        # end_marker

    def maxProduct_messy(self, nums: List[int]) -> int:
        res = nums[0]
        curr_max = None
        curr_neg_max = None
        for n in nums:
            # print(f"i: {i}, n: {n}, curr_max: {curr_max}, curr_neg_max: {curr_neg_max}")
            # print(f"res: {res}")
            if n == 0:
                if curr_max is not None:
                    res = max(res, curr_max)
                    curr_max = None
                if curr_neg_max is not None:
                    curr_neg_max = None
                res = max(res, 0)

                continue
            if n > 0:
                if curr_max is None:
                    curr_max = n
                else:
                    curr_max *= n
                if curr_neg_max is not None:
                    curr_neg_max *= n
                res = max(res, curr_max)
                continue
            # n is negative
            if curr_max is None and curr_neg_max is None:
                curr_neg_max = n
            else:
                if curr_neg_max is None:
                    if curr_max is None:
                        curr_neg_max = n
                    else:
                        res = max(res, curr_max)
                        curr_neg_max = curr_max * n
                        curr_max = None
                    continue
                else:
                    if curr_max is None:
                        curr_max = curr_neg_max * n
                        curr_neg_max = n
                    else:
                        curr_neg_max, curr_max = curr_max * n, curr_neg_max * n
                    res = max(res, curr_max)

        # print(f"res: {res}, curr_max: {curr_max}, curr_neg_max: {curr_neg_max}")
        if curr_max is not None:
            res = max(res, curr_max)
        # print(f"res: {res}")

        return res

    def maxProduct_mayurbhambhani(self, nums: List[int]) -> int:
        res = nums[0]
        curr_max = 1
        for n in nums:
            if n == 0:
                res = max(res, 0)
                curr_max = 1
            else:
                curr_max = curr_max * n
                res = max(res, curr_max)
            print(f"n: {n}, res: {res}, curr_max: {curr_max}")

        curr_max = 1
        for n in nums[::-1]:
            if n == 0:
                curr_max = 1
            else:
                curr_max = curr_max * n
                res = max(res, curr_max)
            print(f"n: {n}, res: {res}, curr_max: {curr_max}")
        return res
        # end_marker


def prod(nums: List[int]) -> int:
    return reduce(lambda x, y: x * y, nums)


class TestSolution(unittest.TestCase):
    def test_case_1(self):
        nums = [2, 3, -2, 4]
        ans = 6
        self.assertEqual(Solution().maxProduct(nums), ans)

    def test_case_2(self):
        nums = [-2, 0, -1]
        ans = 0
        self.assertEqual(Solution().maxProduct(nums), ans)

    def test_case_3(self):
        nums = [0, 2]
        ans = 2
        self.assertEqual(Solution().maxProduct(nums), ans)

    def test_case_4(self):
        nums = [0, 2, 0]
        ans = 2
        self.assertEqual(Solution().maxProduct(nums), ans)

    def test_case_5(self):
        nums = [0, 2, 0, 2]
        ans = 2
        self.assertEqual(Solution().maxProduct(nums), ans)

    def test_case_6(self):
        nums = [-2, 3, -4]
        ans = 24
        self.assertEqual(Solution().maxProduct(nums), ans)

    def test_case_7(self):
        nums = [-2, 3, -4, 5]
        ans = 120
        self.assertEqual(Solution().maxProduct(nums), ans)

    def test_case_8(self):
        nums = [-2, 3, -4, 5, 6]
        ans = prod(nums)
        self.assertEqual(Solution().maxProduct(nums), ans)

    def test_case_9(self):
        nums = [-2, 3, -4, 5, 6, 7]
        ans = prod(nums)
        self.assertEqual(Solution().maxProduct(nums), ans)

    def test_case_10(self):
        nums = [-2, 3, -4, 5, 6, 7, 8]
        ans = prod(nums)
        self.assertEqual(Solution().maxProduct(nums), ans)

    def test_case_11(self):
        nums = [-2, 3, -4, 5, 6, 7, 8, 9]
        ans = prod(nums)
        self.assertEqual(Solution().maxProduct(nums), ans)

    def test_case_12(self):
        nums = [-2, 3, -4, 5, 6, 7, 8, 9, 10]
        ans = prod(nums)
        self.assertEqual(Solution().maxProduct(nums), ans)

    def test_case_13(self):
        nums = [-2, 3, -4, 5, 6, 7, 8, 9, 10, 11]
        ans = prod(nums)
        self.assertEqual(Solution().maxProduct(nums), ans)

    def test_case_14(self):
        nums = [-2, 3, -4, 5, 6, 7, 8, 9, 10, 11, 12]
        ans = prod(nums)
        self.assertEqual(Solution().maxProduct(nums), ans)

    def test_case_15(self):
        nums = [-2, 3, -4, 5, 6, 7, -8, 9, 10, 11, 12, 13]
        ans = prod(nums[1:])
        self.assertEqual(Solution().maxProduct(nums), ans)

    def test_case_16(self):
        nums = [-2, 2, -2, 3, -3]
        ans = prod(nums[1:])
        self.assertEqual(Solution().maxProduct(nums), ans)

    def test_case_17(self):
        nums = [2, -5, -2, -4, 3]
        ans = 24
        self.assertEqual(Solution().maxProduct(nums), ans)

    def test_case_18(self):
        nums = [5, -2, -3, -4, 4]
        ans = 48
        self.assertEqual(Solution().maxProduct(nums), ans)

    def test_case_19(self):
        nums = [5, -2, 3, -3, 7, -4, 8]
        ans = 2016
        self.assertEqual(Solution().maxProduct(nums), ans)

    def test_case_20(self):
        nums = [5, -2, 0, -3, 0, -4, 8, 9]
        ans = 72
        self.assertEqual(Solution().maxProduct(nums), ans)

    def test_case_21(self):
        nums = [-2]
        ans = -2
        self.assertEqual(Solution().maxProduct(nums), ans)

    def test_case_22(self):
        nums = [0]
        ans = 0
        self.assertEqual(Solution().maxProduct(nums), ans)

    def test_case_23(self):
        nums = [2]
        ans = 2
        self.assertEqual(Solution().maxProduct(nums), ans)


if __name__ == "__main__":
    unittest.main()
