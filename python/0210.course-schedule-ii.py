#  Category: algorithms
#  Level: Medium
#  Percent: 49.989693%
# pylint: enable=useless-suppression
# pylint: disable=invalid-name, line-too-long, too-few-public-methods
# pylint: disable=missing-class-docstring, missing-function-docstring, missing-module-docstring


#  There are a total of numCourses courses you have to take, labeled from 0 to
#  numCourses - 1. You are given an array prerequisites where prerequisites[i]
#  = [ai, bi] indicates that you must take course bi first if you want to take
#  course ai.
#
#
#  	For example, the pair [0, 1], indicates that to take course 0 you have to
#  	first take course 1.
#
#
#  Return the ordering of courses you should take to finish all courses. If
#  there are many valid answers, return any of them. If it is impossible to
#  finish all courses, return an empty array.
#
#
#  Example 1:
#
#  Input: numCourses = 2, prerequisites = [[1,0]]
#  Output: [0,1]
#  Explanation: There are a total of 2 courses to take. To take course 1 you
#               should have finished course 0. So the correct course order is [0,1].
#
#
#  Example 2:
#
#  Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
#  Output: [0,2,1,3]
#  Explanation: There are a total of 4 courses to take. To take course 3 you
#               should have finished both courses 1 and 2. Both courses 1 and 2
#               should be taken after you finished course 0.
#  So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3].
#
#
#  Example 3:
#
#  Input: numCourses = 1, prerequisites = []
#  Output: [0]
#
#
#
#  Constraints:
#
#
#  	1 <= numCourses <= 2000
#  	0 <= prerequisites.length <= numCourses * (numCourses - 1)
#  	prerequisites[i].length == 2
#  	0 <= ai, bi < numCourses
#  	ai != bi
#  	All the pairs [ai, bi] are distinct.
#


import unittest
from collections import defaultdict
from typing import DefaultDict, List


#  start_marker
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        in_degree = [0] * numCourses
        taken = [False] * numCourses
        res: List[int] = []
        prereq_dict: DefaultDict = defaultdict(lambda: [])
        for cp in prerequisites:
            class_, prereq = cp
            prereq_dict[prereq].append(class_)
            in_degree[class_] += 1

        print(prereq_dict)
        print(in_degree)
        print(taken)

        while not all(taken):
            classes_with_no_prereqs = [
                i for i, c in enumerate(in_degree) if c == 0 and taken[i] is False
            ]
            print(f"classes_with_no_prereqs: {classes_with_no_prereqs}")
            if not classes_with_no_prereqs:
                return []
            for c in classes_with_no_prereqs:

                print(f"c is {c} dammit")
                fulfilled_list = prereq_dict[c]
                for v in fulfilled_list:
                    print(f"decreasing in_degree for {v}")
                    in_degree[v] -= 1
                res.append(c)
                taken[c] = True
                print(f"class taken {c}")
            print(prereq_dict)
            print(in_degree)
            print(taken)

        return res


#  end_marker
class TestSolution(unittest.TestCase):
    def test_case_1(self):
        numCourses = 2
        prerequisites = [[1, 0]]
        expected = [0, 1]
        result = Solution().findOrder(numCourses, prerequisites)
        self.assertEqual(result, expected)

    def test_case_2(self):
        numCourses = 4
        prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]
        expected = [0, 1, 2, 3]
        result = Solution().findOrder(numCourses, prerequisites)
        self.assertEqual(result, expected)

    def test_case_3(self):
        numCourses = 1
        prerequisites = []
        expected = [0]
        result = Solution().findOrder(numCourses, prerequisites)
        self.assertEqual(result, expected)

    def test_case_4(self):
        numCourses = 2
        prerequisites = [[1, 0], [0, 1]]
        expected = []
        result = Solution().findOrder(numCourses, prerequisites)
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
