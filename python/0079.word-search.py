#  Category: algorithms
#  Level: Medium
#  Percent: 41.23724%
# pylint: enable=useless-suppression
# pylint: disable=invalid-name, line-too-long, too-few-public-methods
# pylint: disable=missing-class-docstring, missing-function-docstring, missing-module-docstring


#  Given an m x n grid of characters board and a string word, return true if word exists in the grid.
#
#  The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.
#
#
#  Example 1:
#
#  Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
#  Output: true
#
#
#  Example 2:
#
#  Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
#  Output: true
#
#
#  Example 3:
#
#  Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
#  Output: false
#
#
#
#  Constraints:
#
#
#  	m == board.length
#  	n = board[i].length
#  	1 <= m, n <= 6
#  	1 <= word.length <= 15
#  	board and word consists of only lowercase and uppercase English letters.
#
#
#
#  Follow up: Could you use search pruning to make your solution faster with a larger board?


import unittest
from collections import Counter, defaultdict

# from pprint import pprint as pp
from typing import Any, List, Set, Tuple


#  start_marker
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # print("--------")
        # print(f"exist({board=}, {word=})")
        bc: Counter[Any] = Counter()
        locmap: defaultdict[List[Tuple[int, int]]] = defaultdict(list)
        for i, line in enumerate(board):
            for j, letter in enumerate(line):
                locmap[letter].append((i, j))
            bc.update(Counter("".join(line)))

        # pp(locmap)

        # print(bc)
        # pp(locmap)
        wc = Counter(word)
        # print(wc)
        if wc.total() > bc.total():
            return False

        # check to see if any letters in word do not appear enough in board
        for letter, count in wc.items():
            bccount = bc[letter]
            if count > bccount:
                return False

        start_letter = word[0]
        end_letter = word[-1]

        if bc[start_letter] > bc[end_letter]:
            start_letter = end_letter
            word = word[::-1]

        # print(f"{start_letter=} {word=}")

        def get_letter(loc: Tuple[int, int]) -> str:
            return board[loc[0]][loc[1]]

        def find_adjacent_letter(
            letter: str, loc: Tuple[int, int], used: Set[Tuple[int, int]]
        ):
            # check above
            res = []
            if loc[0] > 0:
                upward = (loc[0] - 1, loc[1])
                up_letter = get_letter(upward)
                if upward not in used and up_letter == letter:
                    res.append(upward)
            if loc[0] < len(board) - 1:
                downward = (loc[0] + 1, loc[1])
                down_letter = get_letter(downward)
                if downward not in used and down_letter == letter:
                    res.append(downward)

            if loc[1] > 0:
                leftward = (loc[0], loc[1] - 1)
                left_letter = get_letter(leftward)
                if leftward not in used and left_letter == letter:
                    res.append(leftward)

            if loc[1] < len(board[0]) - 1:
                rightward = (loc[0], loc[1] + 1)
                right_letter = get_letter(rightward)
                if rightward not in used and right_letter == letter:
                    res.append(rightward)
            return res

        def find_word(
            curr: Tuple[int, int], letters: str, used: Set[Tuple[int, int]]
        ) -> bool:
            if not letters:
                return True
            # print(f"find_word({letters=},...)")
            locs = find_adjacent_letter(letters[0], curr, used)
            for loc in locs:
                tmp_used = used.copy()
                tmp_used.add(loc)
                if find_word(loc, letters[1:], tmp_used):
                    return True
            return False

        start_points: List[Tuple[int, int]] = locmap[start_letter]
        for curr in start_points:
            # print(f"{curr=}")
            unused: Set[Tuple[int, int]] = set([curr])
            if find_word(curr, word[1:], unused):
                return True
        return False


#  end_marker
class TestSolution(unittest.TestCase):
    def test_case_0(self):
        board = [["a"]]
        word = "abba"
        result = Solution().exist(board, word)
        expected = False
        self.assertEqual(result, expected)

    def test_case_1(self):
        board = [["a", "a"], ["b", "b"]]
        word = "hi"
        result = Solution().exist(board, word)
        expected = False
        self.assertEqual(result, expected)

    def test_case_2(self):
        board = [["a", "a"], ["b", "b"]]
        word = "ab"
        result = Solution().exist(board, word)
        expected = True
        self.assertEqual(result, expected)

    def test_case_3(self):
        board = [["p", "u", "t", "t", "o", "n"]]
        word = "putton"
        expected = True
        result = Solution().exist(board, word)
        self.assertEqual(result, expected)

    def test_case_4(self):
        board = [
            ["a", "b", "c", "c", "a", "a"],
            ["a", "c", "c", "a", "b", "a"],
        ]
        word = "abc"
        expected = True
        result = Solution().exist(board, word)
        self.assertEqual(expected, result)

    def test_case_5(self):
        board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
        word = "ABCCED"
        expected = True
        result = Solution().exist(board, word)
        self.assertEqual(expected, result)

    def test_case_6(self):
        board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
        word = "SEE"
        expected = True
        result = Solution().exist(board, word)
        self.assertEqual(expected, result)

    def test_case_7(self):
        board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
        word = "ABCB"
        expected = False
        result = Solution().exist(board, word)
        self.assertEqual(expected, result)


if __name__ == "__main__":
    unittest.main()
