import unittest
from unittest import TestCase
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output_array = [1 for _ in range(len(nums))]
        running_product = 1
        for i, n in enumerate(nums[:-1]):
            i = i + 1
            running_product *= n
            print(f"{output_array=} {i=} {n=} {running_product=}")
            output_array[i] = running_product
        running_product = 1
        print(f"left done {output_array}")
        for i, n in enumerate(nums[-1:0:-1]):
            i = len(nums) - i - 2
            running_product *= n
            print(f"{output_array=} {i=} {n=} {running_product=}")
            output_array[i] *= running_product
        return output_array


class TestSolution(TestCase):
    def test_productExceptSelf(self):
        test_cases = [
            {
                "name": "[1,2,3,4]",
                "input": [1, 2, 3, 4],
                "expected": [24, 12, 8, 6]
            },
            {
                "name": "[-1,1,0,-3,3]",
                "input": [-1, 1, 0, -3, 3],
                "expected": [0, 0, 9, 0, 0]
            },
        ]
        solution = Solution()
        for ts in test_cases:
            self.assertEqual(
                ts["expected"],
                solution.productExceptSelf(ts["input"]),
                ts["name"]
            )


if __name__ == '__main__':
    # unittest.main()
    solution = Solution()
    print(solution.productExceptSelf([2, 3, 4, 5]))
