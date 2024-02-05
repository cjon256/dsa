#  Category: algorithms
#  Level: Medium
#  Percent: 34.052654%
# pylint: enable=useless-suppression
# pylint: disable=invalid-name, line-too-long, too-few-public-methods
# pylint: disable=missing-class-docstring, missing-function-docstring, missing-module-docstring


#  Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
#
#  Notice that the solution set must not contain duplicate triplets.
#
#
#  Example 1:
#
#  Input: nums = [-1,0,1,2,-1,-4]
#  Output: [[-1,-1,2],[-1,0,1]]
#  Explanation:
#  nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
#  nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
#  nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
#  The distinct triplets are [-1,0,1] and [-1,-1,2].
#  Notice that the order of the output and the order of the triplets does not matter.
#
#
#  Example 2:
#
#  Input: nums = [0,1,1]
#  Output: []
#  Explanation: The only possible triplet does not sum up to 0.
#
#
#  Example 3:
#
#  Input: nums = [0,0,0]
#  Output: [[0,0,0]]
#  Explanation: The only possible triplet sums up to 0.
#
#
#
#  Constraints:
#
#
#  	3 <= nums.length <= 3000
#  	-10⁵ <= nums[i] <= 10⁵
#

import pickle
import unittest
from collections import Counter
from itertools import combinations
from typing import List, Set


#  start_marker
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        def triplet_append(a: int, b: int, c: int) -> None:
            """Append ordered triplet only if not seen before."""
            triplet = sorted([a, b, c])
            # not doing tuple(triplet) because makes typecheckers unhappy
            triple_tuple = (triplet[0], triplet[1], triplet[2])
            if triple_tuple not in triplets_seen_cache:
                triplets.append(triplet)
                triplets_seen_cache.add(triple_tuple)

        if len(nums) < 3:
            return []

        triplets: List[List[int]] = []
        pos_nums: List[int] = []
        neg_nums: List[int] = []
        zero_count = 0
        nums_cache: Set[int] = set()
        triplets_seen_cache: Set[tuple[int, int, int]] = set()
        for num in nums:
            if num == 0:
                zero_count += 1
            elif num > 0:
                pos_nums.append(num)
                nums_cache.add(num)
            else:
                neg_nums.append(num)
                nums_cache.add(num)

        if zero_count > 2:
            triplets.append([0, 0, 0])

        if zero_count > 0:
            for num in nums_cache:
                if -num in nums_cache:
                    triplet_append(-num, 0, num)

        for a, b in combinations(pos_nums, 2):
            c = -(a + b)
            if c in nums_cache:
                triplet_append(a, b, c)

        for a, b in combinations(neg_nums, 2):
            c = -(a + b)
            if c in nums_cache:
                triplet_append(a, b, c)

        return triplets
        # end_marker


class OldSolution:
    def threeSum_third_try(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        triplets = []
        nums_counter = Counter(nums)
        triplets_seen = set()
        all_pairs = combinations(nums, 2)
        for a, b in all_pairs:
            c = -(a + b)
            triplet = sorted([a, b, c])
            if c in nums_counter:
                if f"{triplet}" in triplets_seen:
                    continue
                triplets_seen.add(f"{triplet}")
                if a == c:
                    if b == c:
                        if nums_counter[c] > 2:
                            triplets.append(triplet)
                    elif nums_counter[c] > 1:
                        triplets.append(triplet)
                elif b == c:
                    if nums_counter[c] > 1:
                        triplets.append(triplet)
                else:
                    triplets.append(triplet)
        return triplets

    def threeSum_slowwww(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        triplets = []
        nums.sort()
        seen = set()
        i = 0
        while nums[i] <= 0 and i < len(nums) - 2:
            a = nums[i]
            if a in seen:
                i += 1
                continue
            seen.add(a)
            left = i + 1
            right = len(nums) - 1
            while left < right:
                b = nums[left]
                c = nums[right]
                if a + b + c == 0:
                    triplet = [a, b, c]
                    if triplet not in triplets:
                        triplets.append(triplet)
                    left += 1
                    right -= 1
                elif a + b + c < 0:
                    left += 1
                else:
                    right -= 1
            i += 1
        return triplets


def order_independent_comparison_of_lists_of_lists(
    a: List[List[int]], b: List[List[int]]
) -> bool:
    if len(a) != len(b):
        return False
    sa = sorted([sorted(x) for x in a])
    sb = sorted([sorted(x) for x in b])
    return sa == sb


class TestSolution(unittest.TestCase):
    def test_case_1(self):
        nums = [-1, 0, 1, 2, -1, -4]
        expected = [[-1, -1, 2], [-1, 0, 1]]
        self.assertTrue(
            order_independent_comparison_of_lists_of_lists(
                Solution().threeSum(nums), expected
            )
        )

    def test_case_2(self):
        nums = [0, 1, 1]
        expected = []
        self.assertTrue(
            order_independent_comparison_of_lists_of_lists(
                Solution().threeSum(nums), expected
            )
        )

    def test_case_3(self):
        nums = [0, 0, 0]
        expected = [[0, 0, 0]]
        self.assertTrue(
            order_independent_comparison_of_lists_of_lists(
                Solution().threeSum(nums), expected
            )
        )

    def test_case_4(self):
        nums = [0, 0, 0, 0]
        expected = [[0, 0, 0]]
        self.assertTrue(
            order_independent_comparison_of_lists_of_lists(
                Solution().threeSum(nums), expected
            )
        )

    def test_case_5(self):
        nums = [0, 0, 0, 0, 0]
        expected = [[0, 0, 0]]
        self.assertTrue(
            order_independent_comparison_of_lists_of_lists(
                Solution().threeSum(nums), expected
            )
        )

    def test_case_6(self):
        nums = [0, 0, 0, 0, 0, 0]
        expected = [[0, 0, 0]]
        self.assertTrue(
            order_independent_comparison_of_lists_of_lists(
                Solution().threeSum(nums), expected
            )
        )

    def test_case_7(self):
        nums = [0, -3, 0, 1, 0, 0, 0]
        expected = [[0, 0, 0]]
        self.assertTrue(
            order_independent_comparison_of_lists_of_lists(
                Solution().threeSum(nums), expected
            )
        )

    def test_case_8(self):
        nums = [-2, -3, 0, 1, 2, -1, 3]
        expected = [[-3, 1, 2], [-2, 0, 2], [-2, -1, 3], [-3, 0, 3], [-1, 0, 1]]
        self.assertTrue(
            order_independent_comparison_of_lists_of_lists(
                Solution().threeSum(nums), expected
            )
        )

    def test_case_9(self):
        with open("data/0015_3sum_test_case_9_input.pkl", "rb") as f:
            nums = pickle.load(f)
        with open("data/0015_3sum_test_case_9_output.pkl", "rb") as f:
            expected = pickle.load(f)
        self.assertTrue(
            order_independent_comparison_of_lists_of_lists(
                Solution().threeSum(nums), expected
            )
        )

    def test_case_10(self):
        nums = [-1, 0, 1, 2, -1, -4, -2, -3, 3, 0, 4]
        expected = [
            [-4, 0, 4],
            [-4, 1, 3],
            [-3, -1, 4],
            [-3, 0, 3],
            [-3, 1, 2],
            [-2, -1, 3],
            [-2, 0, 2],
            [-1, -1, 2],
            [-1, 0, 1],
        ]
        self.assertTrue(
            order_independent_comparison_of_lists_of_lists(
                Solution().threeSum(nums), expected
            )
        )


if __name__ == "__main__":
    unittest.main()
