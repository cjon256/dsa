import unittest
from typing import List
from collections import Counter


class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        def cols_with_ones(row: List[int]) -> List[int]:
            cols = []
            for col in range(len(row)):
                if row[col] == 1:
                    cols.append(col)
            return cols

        count = 0
        singular_rows = {}
        cols_seen = Counter()
        for row in range(len(mat)):
            cols = cols_with_ones(mat[row])
            if cols:
                if len(cols) == 1:
                    # singular_row
                    singular_rows[row] = cols[0]
                for col in cols:
                    cols_seen[col] += 1
        for row in singular_rows:
            if cols_seen[singular_rows[row]] == 1:
                count += 1
        return count


class TestSolution(unittest.TestCase):
    def test_numSpecial(self):
        solution = Solution()

        mat1 = [[1, 0, 0], [0, 0, 1], [1, 0, 0]]
        self.assertEqual(solution.numSpecial(mat1), 1)

        mat2 = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
        self.assertEqual(solution.numSpecial(mat2), 3)

        mat3 = [[0, 0, 0, 1], [1, 0, 0, 0],
                [0, 1, 1, 0], [0, 0, 0, 0]]
        self.assertEqual(solution.numSpecial(mat3), 2)

        mat4 = [[0, 0, 0, 0, 0], [1, 0, 0, 0, 0],
                [0, 1, 0, 0, 0], [0, 0, 1, 0, 0],
                [0, 0, 0, 1, 1]]
        self.assertEqual(solution.numSpecial(mat4), 3)

        mat5 = [[0, 0, 0, 0, 0],
                [1, 0, 0, 0, 0],
                [0, 1, 0, 0, 1],
                [0, 0, 1, 0, 0],
                [0, 0, 0, 1, 0]]
        self.assertEqual(solution.numSpecial(mat5), 3)

        mat6 = [[0, 0, 0, 0, 0, 1, 0, 0],
                [0, 0, 0, 0, 1, 0, 0, 1],
                [0, 0, 0, 0, 1, 0, 0, 0],
                [1, 0, 0, 0, 1, 0, 0, 0],
                [0, 0, 1, 1, 0, 0, 0, 0]]
        self.assertEqual(solution.numSpecial(mat6), 1)


if __name__ == '__main__':
    unittest.main()
