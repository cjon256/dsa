#  Category: algorithms
#  Level: Medium
#  Percent: 42.072018%
# pylint: enable=useless-suppression
# pylint: disable=invalid-name, line-too-long, too-few-public-methods
# pylint: disable=missing-class-docstring, missing-function-docstring, missing-module-docstring


#  Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.
#
#  Implement the LRUCache class:
#
#
#  	LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
#  	int get(int key) Return the value of the key if the key exists, otherwise return -1.
#  	void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
#
#
#  The functions get and put must each run in O(1) average time complexity.
#
#
#  Example 1:
#
#  Input
#  ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
#  [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
#  Output
#  [null, null, null, 1, null, -1, null, -1, 3, 4]
#
#  Explanation
#  LRUCache lRUCache = new LRUCache(2);
#  lRUCache.put(1, 1); // cache is {1=1}
#  lRUCache.put(2, 2); // cache is {1=1, 2=2}
#  lRUCache.get(1);    // return 1
#  lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
#  lRUCache.get(2);    // returns -1 (not found)
#  lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
#  lRUCache.get(1);    // return -1 (not found)
#  lRUCache.get(3);    // return 3
#  lRUCache.get(4);    // return 4
#
#
#
#  Constraints:
#
#
#  	1 <= capacity <= 3000
#  	0 <= key <= 10⁴
#  	0 <= value <= 10⁵
#  	At most 2 * 10⁵ calls will be made to get and put.
#


import unittest
from collections import defaultdict, deque
from typing import Dict


#  start_marker
class LRUCache:

    def __init__(self, capacity: int):
        self.recent_queue: deque[int] = deque()
        self.max_capacity = capacity
        self.used_capacity = 0
        self.data: Dict[int, int] = defaultdict(lambda: -1)

    def get(self, key: int) -> int:
        # print(f"data = {self.data}")
        # print(f"recent_queue = {self.recent_queue}")
        if key in self.data:
            self._remove_from_recent_queue(key)
            self.recent_queue.appendleft(key)
            return self.data[key]
        return -1

    def _remove_from_recent_queue(self, key: int) -> None:
        # this will do at most max_capacity work... so, O(1) relative to input
        # ¯\_(ツ)_/¯
        try:
            self.recent_queue.remove(key)
        except ValueError:
            raise

    def put(self, key: int, value: int) -> None:
        if key in self.data:
            self._remove_from_recent_queue(key)
        else:
            self.used_capacity += 1
            if self.used_capacity > self.max_capacity:
                self._purge_least_recent()
        self.recent_queue.appendleft(key)
        # print(f"data = {self.data}")
        # print(f"recent_queue = {self.recent_queue}")
        self.data[key] = value

    def _purge_least_recent(self):
        key_to_purge = self.recent_queue.pop()
        del self.data[key_to_purge]
        self.used_capacity += 1
        #  end_marker


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
class TestSolution(unittest.TestCase):
    def test_case_1(self):
        lRUCache = LRUCache(2)
        lRUCache.put(1, 1)
        lRUCache.put(2, 2)
        self.assertEqual(lRUCache.get(1), 1)

    def test_case_2(self):
        lRUCache = LRUCache(2)
        lRUCache.put(1, 1)
        print(lRUCache.recent_queue)
        lRUCache.put(2, 2)
        print(lRUCache.recent_queue)
        lRUCache.get(1)
        print(lRUCache.data)
        print(lRUCache.recent_queue)
        lRUCache.put(3, 3)
        print(lRUCache.data)
        self.assertEqual(lRUCache.get(2), -1)

    def test_case_3(self):
        lRUCache = LRUCache(2)
        lRUCache.put(1, 1)
        lRUCache.put(2, 2)
        lRUCache.get(1)
        lRUCache.put(3, 3)
        lRUCache.get(2)
        lRUCache.put(4, 4)
        self.assertEqual(lRUCache.get(1), -1)

    def test_case_4(self):
        lRUCache = LRUCache(2)
        lRUCache.put(1, 1)
        lRUCache.put(2, 2)
        lRUCache.get(1)
        lRUCache.put(3, 3)
        lRUCache.get(2)
        lRUCache.put(4, 4)
        lRUCache.get(1)
        self.assertEqual(lRUCache.get(3), 3)

    def test_case_5(self):
        lRUCache = LRUCache(2)
        lRUCache.put(1, 1)
        lRUCache.put(2, 2)
        lRUCache.get(1)
        lRUCache.put(3, 3)
        lRUCache.get(2)
        lRUCache.put(4, 4)
        lRUCache.get(1)
        lRUCache.get(3)
        self.assertEqual(lRUCache.get(4), 4)

    def test_case_6(self):
        lru = LRUCache(2)
        lru.put(2, 1)
        lru.put(2, 2)
        lru.get(2)
        lru.put(1, 1)
        lru.put(4, 1)
        lru.get(2)

    def test_case_7(self):
        null = None
        # fmt: off
        actions = [ "put", "put", "put", "put", "put", "get", "put", "get", "get", "put", "get", "put", "put", "put", "get", "put", "get", "get", "get", "get", "put", "put", "get", "get", "get", "put", "put", "get", "put", "get", "put", "get", "get", "get", "put", "put", "put", "get", "put", "get", "get", "put", "put", "get", "put", "put", "put", "put", "get", "put", "put", "get", "put", "put", "get", "put", "put", "put", "put", "put", "get", "put", "put", "get", "put", "get", "get", "get", "put", "get", "get", "put", "put", "put", "put", "get", "put", "put", "put", "put", "get", "get", "get", "put", "put", "put", "get", "put", "put", "put", "get", "put", "put", "put", "get", "get", "get", "put", "put", "put", "put", "get", "put", "put", "put", "put", "put", "put", "put", ]
        args = [ [10, 13], [3, 17], [6, 11], [10, 5], [9, 10], [13], [2, 19], [2], [3], [5, 25], [8], [9, 22], [5, 5], [1, 30], [11], [9, 12], [7], [5], [8], [9], [4, 30], [9, 3], [9], [10], [10], [6, 14], [3, 1], [3], [10, 11], [8], [2, 14], [1], [5], [4], [11, 4], [12, 24], [5, 18], [13], [7, 23], [8], [12], [3, 27], [2, 12], [5], [2, 9], [13, 4], [8, 18], [1, 7], [6], [9, 29], [8, 21], [5], [6, 30], [1, 12], [10], [4, 15], [7, 22], [11, 26], [8, 17], [9, 29], [5], [3, 4], [11, 30], [12], [4, 29], [3], [9], [6], [3, 4], [1], [10], [3, 29], [10, 28], [1, 20], [11, 13], [3], [3, 12], [3, 8], [10, 9], [3, 26], [8], [7], [5], [13, 17], [2, 27], [11, 15], [12], [9, 19], [2, 15], [3, 16], [1], [12, 17], [9, 1], [6, 19], [4], [5], [5], [8, 1], [11, 7], [5, 2], [9, 28], [1], [2, 2], [7, 4], [4, 22], [7, 24], [9, 26], [13, 28], [11, 26], ]
        expected = [ null, null, null, null, null, -1, null, 19, 17, null, -1, null, null, null, -1, null, -1, 5, -1, 12, null, null, 3, 5, 5, null, null, 1, null, -1, null, 30, 5, 30, null, null, null, -1, null, -1, 24, null, null, 18, null, null, null, null, -1, null, null, 18, null, null, -1, null, null, null, null, null, 18, null, null, -1, null, 4, 29, 30, null, 12, -1, null, null, null, null, 29, null, null, null, null, 17, 22, 18, null, null, null, -1, null, null, null, 20, null, null, null, -1, 18, 18, null, null, null, null, 20, null, null, null, null, null, null, null, ]
        # fmt: on
        lru = LRUCache(10)
        for act, arg, exp in zip(actions, args, expected):
            print(f"lru.{act}({', '.join(map(str,arg))})")
            method = getattr(lru, act)
            val = method(*arg)
            print(
                f"expected = {exp}, val = {val} {'*****************' if val != exp else ''}"
            )


if __name__ == "__main__":
    unittest.main()
