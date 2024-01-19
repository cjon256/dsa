import unittest

DEBUG = False


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        note_letters = list(magazine)
        for i in ransomNote:
            if DEBUG:
                print(i)
            if i in note_letters:
                if DEBUG:
                    print(f"{i} in {note_letters}")
                note_letters.remove(i)
            else:
                if DEBUG:
                    print(f"{i} not in {note_letters}")
                return False
        return True


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
