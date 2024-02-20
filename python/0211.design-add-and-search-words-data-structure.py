#  Category: algorithms
#  Level: Medium
#  Percent: 44.839756%
# pylint: enable=useless-suppression
# pylint: disable=invalid-name, line-too-long, too-few-public-methods
# pylint: disable=missing-class-docstring, missing-function-docstring, missing-module-docstring


#  Design a data structure that supports adding new words and finding if a
#  string matches any previously added string.
#
#  Implement the WordDictionary class:
#
#
#  	WordDictionary() Initializes the object.
#  	void addWord(word) Adds word to the data structure, it can be matched later.
#  	bool search(word) Returns true if there is any string in the data structure
#  	that matches word or false otherwise. word may contain dots '.' where dots
#  	can be matched with any letter.
#
#
#
#  Example:
#
#  Input
#  ["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
#  [[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
#  Output
#  [null,null,null,null,false,true,true,true]
#
#  Explanation
#  WordDictionary wordDictionary = new WordDictionary();
#  wordDictionary.addWord("bad");
#  wordDictionary.addWord("dad");
#  wordDictionary.addWord("mad");
#  wordDictionary.search("pad"); // return False
#  wordDictionary.search("bad"); // return True
#  wordDictionary.search(".ad"); // return True
#  wordDictionary.search("b.."); // return True
#
#
#
#  Constraints:
#
#
#  	1 <= word.length <= 25
#  	word in addWord consists of lowercase English letters.
#  	word in search consist of '.' or lowercase English letters.
#  	There will be at most 2 dots in word for search queries.
#  	At most 10⁴ calls will be made to addWord and search.
#
# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

import unittest
from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Self


@dataclass
class TrieNode:
    present: bool
    children: List[Optional[Self]]

    def __init__(self):
        self.present = False
        self.children = [None] * 26


class WordDictionaryTrie:
    def __init__(self):
        self.trie: TrieNode = TrieNode()

    def addWord(self, word: str) -> None:
        curr_node: TrieNode = self.trie
        for letter in word:
            index = ord(letter) - ord("a")
            if not curr_node.children[index]:
                curr_node.children[index] = TrieNode()
            curr_node = curr_node.children[index]
        curr_node.present = True

    def search(self, word: str) -> bool:
        def recur(remaining, curr_node) -> bool:
            if remaining == "":
                return curr_node.present
            letter = remaining[0]
            if letter == ".":
                for child in curr_node.children:
                    if not child:
                        continue
                    if recur(remaining[1:], child):
                        return True
                return False
            index = ord(letter) - ord("a")
            if not curr_node.children[index]:
                return False
            next_node = curr_node.children[index]
            return recur(remaining[1:], next_node)

        return recur(word, self.trie)


#  start_marker
class WordDictionary:
    def __init__(self):
        self.trie: Dict[str, Any] = {}

    def addWord(self, word: str) -> None:
        curr_dict = self.trie
        for letter in word:
            if letter not in curr_dict:
                curr_dict[letter] = {}
            curr_dict = curr_dict[letter]
        curr_dict["#"] = True

    def search(self, word: str) -> bool:
        def recur(remaining, curr_dict) -> bool:
            if remaining == "":
                return "#" in curr_dict
            letter = remaining[0]
            if letter == ".":
                for k in curr_dict:
                    if k == "#":
                        continue
                    if recur(remaining[1:], curr_dict[k]):
                        return True
                return False
            if letter not in curr_dict:
                return False
            next_dict = curr_dict[letter]
            return recur(remaining[1:], next_dict)

        return recur(word, self.trie)
        #  end_marker


class TestSolution1(unittest.TestCase):
    def setUp(self):
        self.obj = WordDictionary()
        self.obj.addWord("hello")
        self.obj.addWord("hell")
        self.obj.addWord("hi")

    def test_case_1(self):
        self.assertTrue(self.obj.search("hello"))

    def test_case_2(self):
        self.assertFalse(self.obj.search("ho"))

    def test_case_3(self):
        self.assertTrue(self.obj.search("h.ll."))

    def test_case_4(self):
        self.assertTrue(self.obj.search(".."))

    def test_case_5(self):
        self.assertTrue(self.obj.search(".el."))


class TestSolution2(unittest.TestCase):
    def setUp(self):
        self.obj = WordDictionary()
        self.obj.addWord("bad")
        self.obj.addWord("dad")
        self.obj.addWord("mad")

    def test_case_1(self):
        self.assertFalse(self.obj.search("pad"))

    def test_case_2(self):
        self.assertTrue(self.obj.search("bad"))

    def test_case_3(self):
        self.assertTrue(self.obj.search(".ad"))

    def test_case_4(self):
        self.assertTrue(self.obj.search("b.."))


class TestSolution3(unittest.TestCase):
    def setUp(self):
        self.obj = WordDictionary()
        self.obj.addWord("a")
        self.obj.addWord("a")

    def test_case_1(self):
        self.assertTrue(self.obj.search("."))

    def test_case_2(self):
        self.assertTrue(self.obj.search("a"))

    def test_case_3(self):
        self.assertFalse(self.obj.search("aa"))

    def test_case_4(self):
        self.assertFalse(self.obj.search("a."))

    def test_case_5(self):
        self.assertFalse(self.obj.search(".a"))

    def test_case_6(self):
        self.assertFalse(self.obj.search("a.a"))

    def test_case_7(self):
        self.assertFalse(self.obj.search("b"))


if __name__ == "__main__":
    unittest.main()
