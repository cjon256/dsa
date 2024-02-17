#  Category: algorithms
#  Level: Medium
#  Percent: 58.111877%
# pylint: enable=useless-suppression
# pylint: disable=invalid-name, line-too-long, too-few-public-methods
# pylint: disable=missing-class-docstring, missing-function-docstring, missing-module-docstring


#  Given a characters array tasks, representing the tasks a CPU needs to do, where each letter represents a different task. Tasks could be done in any order. Each task is done in one unit of time. For each unit of time, the CPU could complete either one task or just be idle.
#
#  However, there is a non-negative integer n that represents the cooldown period between two same tasks (the same letter in the array), that is that there must be at least n units of time between any two same tasks.
#
#  Return the least number of units of times that the CPU will take to finish all the given tasks.
#
#
#  Example 1:
#
#  Input: tasks = ["A","A","A","B","B","B"], n = 2
#  Output: 8
#  Explanation:
#  A -> B -> idle -> A -> B -> idle -> A -> B
#  There is at least 2 units of time between any two same tasks.
#
#
#  Example 2:
#
#  Input: tasks = ["A","A","A","B","B","B"], n = 0
#  Output: 6
#  Explanation: On this case any permutation of size 6 would work since n = 0.
#  ["A","A","A","B","B","B"]
#  ["A","B","A","B","A","B"]
#  ["B","B","B","A","A","A"]
#  ...
#  And so on.
#
#
#  Example 3:
#
#  Input: tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"], n = 2
#  Output: 16
#  Explanation:
#  One possible solution is
#  A -> B -> C -> A -> D -> E -> A -> F -> G -> A -> idle -> idle -> A -> idle -> idle -> A
#
#
#
#  Constraints:
#
#
#  	1 <= task.length <= 10⁴
#  	tasks[i] is upper-case English letter.
#  	The integer n is in the range [0, 100].
#

import unittest
from pprint import pprint as pp
from typing import List


#  start_marker
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        num_left = [0] * 26
        cooldowns = [0] * 26

        def tick_cooldown():
            for i in range(26):
                if cooldowns[i] > 0:
                    cooldowns[i] -= 1

        for task in tasks:
            num_left[ord(task) - ord("A")] += 1

        turns_taken = 0

        max_i = None

        while sum(num_left) > 0:
            # find best job
            max_t, max_i = 0, None
            for i, t in enumerate(num_left):
                if t > max_t:
                    # print("num_left", end=" ")
                    # pp(num_left)
                    # print("cooldowns", end=" ")
                    # pp(cooldowns)
                    if cooldowns[i] == 0:
                        max_t = t
                        max_i = i

            # print(f"{max_i=} {max_t=}")

            turns_taken += 1
            tick_cooldown()

            # check if we need to pass
            if max_i is None:
                continue

            # process the job
            num_left[max_i] -= 1
            cooldowns[max_i] = n

        return turns_taken
        #  end_marker


class TestSolution(unittest.TestCase):
    def test_case_1(self):
        tasks = ["A", "A", "A", "B", "B", "B"]
        n = 0
        expected = 6
        result = Solution().leastInterval(tasks, n)
        self.assertEqual(result, expected)

    def test_case_2(self):
        tasks = ["A", "A", "A", "B", "B", "B"]
        n = 2
        expected = 8
        result = Solution().leastInterval(tasks, n)
        self.assertEqual(result, expected)

    def test_case_3(self):
        tasks = ["A", "A", "A", "A", "A", "A", "B", "C", "D", "E", "F", "G"]
        n = 2
        expected = 16
        result = Solution().leastInterval(tasks, n)
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
