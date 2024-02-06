#  Category: algorithms
#  Level: Medium
#  Percent: 46.487217%
# pylint: enable=useless-suppression
# pylint: disable=invalid-name, line-too-long, too-few-public-methods
# pylint: disable=missing-class-docstring, missing-function-docstring, missing-module-docstring


#  There are a total of numCourses courses you have to take, labeled from 0 to
#  numCourses - 1. You are given an array prerequisites where prerequisites[i]
#  = [ai, bi] indicates that you must take course bi first if you want to take
#  course ai.
#
#
#  	For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
#
#
#  Return true if you can finish all courses. Otherwise, return false.
#
#
#  Example 1:
#
#  Input: numCourses = 2, prerequisites = [[1,0]]
#  Output: true
#  Explanation: There are a total of 2 courses to take.
#  To take course 1 you should have finished course 0. So it is possible.
#
#
#  Example 2:
#
#  Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
#  Output: false
#  Explanation: There are a total of 2 courses to take.
#  To take course 1 you should have finished course 0, and to take course 0 you
#  should also have finished course 1. So it is impossible.
#
#
#
#  Constraints:
#
#
#  	1 <= numCourses <= 2000
#  	0 <= prerequisites.length <= 5000
#  	prerequisites[i].length == 2
#  	0 <= ai, bi < numCourses
#  	All the pairs prerequisites[i] are unique.
#

import unittest

#  start_marker
from collections import defaultdict
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites:
            return True

        dependency_graph: defaultdict[int, List[int]] = defaultdict(list)
        courses_of_interest = []
        in_degree = [0] * numCourses
        prereqs = set()
        for course, prerequisite in prerequisites:
            dependency_graph[prerequisite].append(course)
            in_degree[course] = in_degree[course] + 1
            prereqs.add(prerequisite)
        for course in prereqs:
            if in_degree[course] == 0:
                courses_of_interest.append(course)
        while courses_of_interest:
            course = courses_of_interest.pop()
            for dependent_course in dependency_graph[course]:
                in_degree[dependent_course] = in_degree[dependent_course] - 1
                if in_degree[dependent_course] == 0:
                    courses_of_interest.append(dependent_course)
        return sum(in_degree) == 0


#  end_marker
class TestSolution(unittest.TestCase):
    def test_case_1(self):
        numCourses = 2
        prerequisites = [[1, 0]]
        expected_result = True
        self.assertEqual(
            Solution().canFinish(numCourses, prerequisites), expected_result
        )

    def test_case_2(self):
        numCourses = 2
        prerequisites = [[1, 0], [0, 1]]
        expected_result = False
        self.assertEqual(
            Solution().canFinish(numCourses, prerequisites), expected_result
        )

    def test_case_3(self):
        numCourses = 3
        prerequisites = [[1, 0], [2, 1]]
        expected_result = True
        self.assertEqual(
            Solution().canFinish(numCourses, prerequisites), expected_result
        )

    def test_case_4(self):
        numCourses = 100
        prerequisites = [
            [1, 2],
            [2, 3],
            [7, 8],
            [34, 56],
            [23, 45],
            [12, 34],
            [56, 78],
            [45, 67],
            [78, 89],
            [67, 12],
            [89, 12],
        ]
        expected_result = False
        self.assertEqual(
            Solution().canFinish(numCourses, prerequisites), expected_result
        )

    def test_case_5(self):
        numCourses = 3
        prerequisites = [[1, 0], [2, 1], [0, 2]]
        expected_result = False
        self.assertEqual(
            Solution().canFinish(numCourses, prerequisites), expected_result
        )

    def test_case_6(self):
        numCourses = 3
        prerequisites = [[1, 0], [0, 2], [1, 2]]
        expected_result = True
        self.assertEqual(
            Solution().canFinish(numCourses, prerequisites), expected_result
        )

    def test_case_7(self):
        numCourses = 5
        prerequisites = [[1, 4], [2, 4], [3, 1], [3, 2]]
        expected_result = True
        self.assertEqual(
            Solution().canFinish(numCourses, prerequisites), expected_result
        )


if __name__ == "__main__":
    unittest.main()
