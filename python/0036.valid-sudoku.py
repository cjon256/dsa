#  Category: algorithms
#  Level: Medium
#  Percent: 59.169662%


#  Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
#
#
#  	Each row must contain the digits 1-9 without repetition.
#  	Each column must contain the digits 1-9 without repetition.
#  	Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
#
#
#  Note:
#
#
#  	A Sudoku board (partially filled) could be valid but is not necessarily solvable.
#  	Only the filled cells need to be validated according to the mentioned rules.
#
#
#
#  Example 1:
#
#  Input: board =
#  [["5","3",".",".","7",".",".",".","."]
#  ,["6",".",".","1","9","5",".",".","."]
#  ,[".","9","8",".",".",".",".","6","."]
#  ,["8",".",".",".","6",".",".",".","3"]
#  ,["4",".",".","8",".","3",".",".","1"]
#  ,["7",".",".",".","2",".",".",".","6"]
#  ,[".","6",".",".",".",".","2","8","."]
#  ,[".",".",".","4","1","9",".",".","5"]
#  ,[".",".",".",".","8",".",".","7","9"]]
#  Output: true
#
#
#  Example 2:
#
#  Input: board =
#  [["8","3",".",".","7",".",".",".","."]
#  ,["6",".",".","1","9","5",".",".","."]
#  ,[".","9","8",".",".",".",".","6","."]
#  ,["8",".",".",".","6",".",".",".","3"]
#  ,["4",".",".","8",".","3",".",".","1"]
#  ,["7",".",".",".","2",".",".",".","6"]
#  ,[".","6",".",".",".",".","2","8","."]
#  ,[".",".",".","4","1","9",".",".","5"]
#  ,[".",".",".",".","8",".",".","7","9"]]
#  Output: false
#  Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.
#
#
#
#  Constraints:
#
#
#  	board.length == 9
#  	board[i].length == 9
#  	board[i][j] is a digit 1-9 or '.'.
#


import unittest
from typing import List


#  start_marker
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def cell_to_box(i, j):
            return (i // 3) * 3 + j // 3

        rows = [set() for _ in range(9)]
        columns = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                element = board[i][j]
                if element == ".":
                    continue
                if (
                    element in rows[i]
                    or element in columns[j]
                    or element in boxes[cell_to_box(i, j)]
                ):
                    return False
                rows[i].add(element)
                columns[j].add(element)
                boxes[cell_to_box(i, j)].add(element)
        return True

    def isValidSudoku_old(self, board: List[List[str]]) -> bool:
        def get_three_by_three(board, i):
            start_x = i // 3 * 3
            start_y = i % 3 * 3
            three_by_three = []
            for x in range(0, 3):
                for y in range(0, 3):
                    element = board[start_x + x][start_y + y]
                    if element != ".":
                        three_by_three.append(element)
            return three_by_three

        def validate(box):
            if not box:
                return True
            return len(box) == len(set(box))

        for i in range(len(board)):
            row = [x for x in board[i] if x != "."]
            if not validate(row):
                return False
            column = [x[i] for x in board if x[i] != "."]
            if not validate(column):
                return False
            three_by_three = get_three_by_three(board, i)
            if not validate(three_by_three):
                return False
        return True


#  end_marker
class TestSolution(unittest.TestCase):
    def test_case_1(self):
        board = [
            ["5", "3", ".", ".", "7", ".", ".", ".", "."],
            ["6", ".", ".", "1", "9", "5", ".", ".", "."],
            [".", "9", "8", ".", ".", ".", ".", "6", "."],
            ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
            ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
            ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
            [".", "6", ".", ".", ".", ".", "2", "8", "."],
            [".", ".", ".", "4", "1", "9", ".", ".", "5"],
            [".", ".", ".", ".", "8", ".", ".", "7", "9"],
        ]
        result = Solution().isValidSudoku(board)
        self.assertEqual(result, True)

    def test_case_2(self):
        board = [
            ["8", "3", ".", ".", "7", ".", ".", ".", "."],
            ["6", ".", ".", "1", "9", "5", ".", ".", "."],
            [".", "9", "8", ".", ".", ".", ".", "6", "."],
            ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
            ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
            ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
            [".", "6", ".", ".", ".", ".", "2", "8", "."],
            [".", ".", ".", "4", "1", "9", ".", ".", "5"],
            [".", ".", ".", ".", "8", ".", ".", "7", "9"],
        ]
        result = Solution().isValidSudoku(board)
        self.assertEqual(result, False)

    def test_case_3(self):
        """completely empty board"""
        board = [["." for _ in range(9)] for _ in range(9)]
        result = Solution().isValidSudoku(board)
        self.assertEqual(result, True)

    def test_case_4(self):
        """completely full board"""
        board = [
            ["1", "2", "3", "4", "5", "6", "7", "8", "9"],
            ["4", "5", "6", "7", "8", "9", "1", "2", "3"],
            ["7", "8", "9", "1", "2", "3", "4", "5", "6"],
            ["2", "3", "4", "5", "6", "7", "8", "9", "1"],
            ["5", "6", "7", "8", "9", "1", "2", "3", "4"],
            ["8", "9", "1", "2", "3", "4", "5", "6", "7"],
            ["3", "4", "5", "6", "7", "8", "9", "1", "2"],
            ["6", "7", "8", "9", "1", "2", "3", "4", "5"],
            ["9", "1", "2", "3", "4", "5", "6", "7", "8"],
        ]
        result = Solution().isValidSudoku(board)
        self.assertEqual(result, True)

    def test_case_5(self):
        """completely full board with one invalid row"""
        board = [
            ["1", "2", "3", "4", "5", "6", "7", "8", "9"],
            ["4", "5", "6", "7", "8", "9", "1", "2", "3"],
            ["7", "8", "9", "1", "2", "3", "4", "5", "6"],
            ["2", "3", "4", "5", "6", "7", "8", "9", "1"],
            ["5", "6", "7", "8", "9", "1", "2", "3", "4"],
            ["8", "9", "1", "2", "3", "4", "5", "6", "7"],
            ["3", "4", "5", "6", "7", "8", "9", "1", "2"],
            ["6", "7", "8", "9", "1", "2", "3", "4", "5"],
            ["9", "1", "2", "3", "4", "5", "6", "7", "1"],
        ]
        result = Solution().isValidSudoku(board)
        self.assertEqual(result, False)

    def test_case_6(self):
        """completely full board with one invalid column"""
        board = [
            ["1", "2", "3", "4", "5", "6", "7", "8", "9"],
            ["4", "5", "6", "7", "8", "9", "1", "2", "3"],
            ["7", "8", "9", "1", "2", "3", "4", "5", "6"],
            ["2", "3", "4", "5", "6", "7", "8", "9", "1"],
            ["5", "6", "7", "8", "9", "1", "2", "3", "4"],
            ["8", "9", "1", "2", "3", "4", "5", "6", "7"],
            ["3", "4", "5", "6", "7", "8", "9", "1", "2"],
            ["6", "7", "8", "9", "1", "2", "3", "4", "5"],
            ["9", "1", "2", "3", "4", "5", "6", "7", "1"],
        ]
        result = Solution().isValidSudoku(board)
        self.assertEqual(result, False)

    def test_case_7(self):
        """completely full board with one invalid 3x3 box"""
        board = [
            ["1", "2", "3", "4", "5", "6", "7", "8", "9"],
            ["4", "5", "6", "7", "8", "9", "1", "2", "3"],
            ["7", "8", "9", "1", "2", "3", "4", "5", "6"],
            ["2", "3", "4", "5", "6", "7", "8", "9", "1"],
            ["5", "6", "7", "8", "9", "1", "2", "3", "4"],
            ["8", "9", "1", "2", "3", "4", "5", "6", "7"],
            ["3", "4", "5", "6", "7", "8", "9", "1", "2"],
            ["6", "7", "8", "9", "1", "2", "3", "4", "5"],
            ["9", "1", "2", "3", "4", "5", "6", "7", "1"],
        ]
        result = Solution().isValidSudoku(board)
        self.assertEqual(result, False)

    def test_case_8(self):
        """board with one element in each row, column, and 3x3 box"""
        board = [
            ["1", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", "2", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", "3", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", "4", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", "5", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", "6", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", "7", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "8", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", "9"],
        ]
        result = Solution().isValidSudoku(board)
        self.assertEqual(result, True)

    def test_case_9(self):
        board = [
            [".", ".", ".", ".", "5", ".", ".", "1", "."],
            [".", "4", ".", "3", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", "3", ".", ".", "1"],
            ["8", ".", ".", ".", ".", ".", ".", "2", "."],
            [".", ".", "2", ".", "7", ".", ".", ".", "."],
            [".", "1", "5", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", "2", ".", ".", "."],
            [".", "2", ".", "9", ".", ".", ".", ".", "."],
            [".", ".", "4", ".", ".", ".", ".", ".", "."],
        ]
        result = Solution().isValidSudoku(board)
        self.assertEqual(result, False)


if __name__ == "__main__":
    unittest.main()
