#  Category: algorithms
#  Level: Easy
#  Percent: 60.61229%
# pylint: enable=useless-suppression
# pylint: disable=invalid-name, line-too-long, too-few-public-methods
# pylint: disable=missing-class-docstring, missing-function-docstring, missing-module-docstring


#  Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.
#
#  Each letter in magazine can only be used once in ransomNote.
#
#
#  Example 1:
#  Input: ransomNote = "a", magazine = "b"
#  Output: false
#  Example 2:
#  Input: ransomNote = "aa", magazine = "ab"
#  Output: false
#  Example 3:
#  Input: ransomNote = "aa", magazine = "aab"
#  Output: true
#
#
#  Constraints:
#
#
#  	1 <= ransomNote.length, magazine.length <= 10⁵
#  	ransomNote and magazine consist of lowercase English letters.
#

import unittest


#  start_marker
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        note_letters = list(magazine)
        for i in ransomNote:
            # print(i)
            if i in note_letters:
                # print(f"{i} in {note_letters}")
                note_letters.remove(i)
            else:
                # print(f"{i} not in {note_letters}")
                return False
        return True
        #  end_marker


DEBUG = False


class Test(unittest.TestCase):
    def test1(self):
        if DEBUG:
            print("test1")
        self.assertEqual(Solution().canConstruct("a", "b"), False)

    def test2(self):
        if DEBUG:
            print("test2")
        self.assertEqual(Solution().canConstruct("aa", "ab"), False)

    def test3(self):
        if DEBUG:
            print("test3")
        self.assertEqual(Solution().canConstruct("aa", "aab"), True)

    def test4(self):
        if DEBUG:
            print("test4")
        self.assertEqual(Solution().canConstruct("ba", "ab"), True)

    def test5(self):
        if DEBUG:
            print("test5")
        self.assertEqual(Solution().canConstruct("aa", "aba"), True)

    def test6(self):
        if DEBUG:
            print("test6")
        self.assertEqual(
            Solution().canConstruct("acocccaccecca", "cccccooeeaabaaccc"), True
        )


if __name__ == "__main__":
    unittest.main()
