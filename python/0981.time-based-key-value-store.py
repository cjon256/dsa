#  Category: algorithms
#  Level: Medium
#  Percent: 49.751614%
# pylint: enable=useless-suppression
# pylint: disable=invalid-name, line-too-long, too-few-public-methods
# pylint: disable=missing-class-docstring, missing-function-docstring, missing-module-docstring


#  Design a time-based key-value data structure that can store multiple values for the same key at different time stamps and retrieve the key's value at a certain timestamp.
#
#  Implement the TimeMap class:
#
#
#  	TimeMap() Initializes the object of the data structure.
#  	void set(String key, String value, int timestamp) Stores the key key with the value value at the given time timestamp.
#  	String get(String key, int timestamp) Returns a value such that set was called previously, with timestamp_prev <= timestamp. If there are multiple such values, it returns the value associated with the largest timestamp_prev. If there are no values, it returns "".
#
#
#
#  Example 1:
#
#  Input
#  ["TimeMap", "set", "get", "get", "set", "get", "get"]
#  [[], ["foo", "bar", 1], ["foo", 1], ["foo", 3], ["foo", "bar2", 4], ["foo", 4], ["foo", 5]]
#  Output
#  [null, null, "bar", "bar", null, "bar2", "bar2"]
#
#  Explanation
#  TimeMap timeMap = new TimeMap();
#  timeMap.set("foo", "bar", 1);  // store the key "foo" and value "bar" along with timestamp = 1.
#  timeMap.get("foo", 1);         // return "bar"
#  timeMap.get("foo", 3);         // return "bar", since there is no value corresponding to foo at timestamp 3 and timestamp 2, then the only value is at timestamp 1 is "bar".
#  timeMap.set("foo", "bar2", 4); // store the key "foo" and value "bar2" along with timestamp = 4.
#  timeMap.get("foo", 4);         // return "bar2"
#  timeMap.get("foo", 5);         // return "bar2"
#
#
#
#  Constraints:
#
#
#  	1 <= key.length, value.length <= 100
#  	key and value consist of lowercase English letters and digits.
#  	1 <= timestamp <= 10⁷
#  	All the timestamps timestamp of set are strictly increasing.
#  	At most 2 * 10⁵ calls will be made to set and get.
#

import unittest
from collections import defaultdict
from typing import List


#  start_marker
class TimeMap:

    def __init__(self):
        self._data = defaultdict(lambda: [[], []])

    def set(self, key: str, value: str, timestamp: int) -> None:
        vals, timestamps = self._data[key]
        vals.append(value)
        timestamps.append(timestamp)

    def get(self, key: str, timestamp: int) -> str:
        def _binary_search(arr: List[int]) -> int:
            left = 0
            right = len(arr) - 1
            while left <= right:
                mid = (left + right) // 2
                if arr[mid] == timestamp:
                    return mid
                elif arr[mid] < timestamp:
                    left = mid + 1
                else:
                    right = mid - 1
            return right

        vals, timestamps = self._data[key]
        if not timestamps:
            return ""
        if timestamp < timestamps[0]:
            return ""
        if timestamp >= timestamps[-1]:
            return vals[-1]
        idx = _binary_search(timestamps)
        return vals[idx]


#  end_marker


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
class TestSolution(unittest.TestCase):
    def test_case_1(self):
        solution = TimeMap()
        solution.set("foo", "bar", 1)
        self.assertEqual(solution.get("foo", 1), "bar")

    def test_case_2(self):
        solution = TimeMap()
        solution.set("foo", "bar", 1)
        self.assertEqual(solution.get("foo", 3), "bar")

    def test_case_3(self):
        solution = TimeMap()
        solution.set("foo", "bar", 1)
        solution.set("foo", "bar2", 4)
        self.assertEqual(solution.get("foo", 4), "bar2")

    def test_case_4(self):
        solution = TimeMap()
        solution.set("foo", "bar", 1)
        solution.set("foo", "bar2", 4)
        self.assertEqual(solution.get("foo", 5), "bar2")

    def test_case_5(self):
        solution = TimeMap()
        solution.set("love", "high", 10)
        solution.set("love", "low", 20)
        self.assertEqual(solution.get("love", 5), "")
        self.assertEqual(solution.get("love", 10), "high")
        self.assertEqual(solution.get("love", 15), "high")
        self.assertEqual(solution.get("love", 20), "low")
        self.assertEqual(solution.get("love", 25), "low")

    def test_case_6(self):
        solution = TimeMap()
        solution.set("love", "high", 10)
        solution.set("love", "low", 20)
        self.assertEqual(solution.get("dog", 5), "")
        self.assertEqual(solution.get("dog", 10), "")
        self.assertEqual(solution.get("dog", 15), "")
        self.assertEqual(solution.get("dog", 20), "")
        self.assertEqual(solution.get("dog", 25), "")

    def test_case_7(self):
        solution = TimeMap()
        solution.set("love", "high", 10)
        solution.set("love", "mid", 15)
        solution.set("love", "low", 20)
        self.assertEqual(solution.get("love", 5), "")
        self.assertEqual(solution.get("love", 10), "high")
        self.assertEqual(solution.get("love", 15), "mid")
        self.assertEqual(solution.get("love", 20), "low")
        self.assertEqual(solution.get("love", 25), "low")


if __name__ == "__main__":
    unittest.main()
