import unittest
from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        return Counter(t) == Counter(s)


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_isAnagram(self):
        self.assertTrue(self.solution.isAnagram('anagram', 'nagaram'))
        self.assertFalse(self.solution.isAnagram('rat', 'car'))


if __name__ == '__main__':
    unittest.main()
