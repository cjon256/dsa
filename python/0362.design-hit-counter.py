#  Category: algorithms
#  Level: Medium
#  Percent: 68.59659%
# pylint: enable=useless-suppression
# pylint: disable=invalid-name, line-too-long, too-few-public-methods
# pylint: disable=missing-class-docstring, missing-function-docstring, missing-module-docstring


#  Design a hit counter which counts the number of hits received in the past 5 minutes (i.e., the past 300 seconds).
#
#  Your system should accept a timestamp parameter (in seconds granularity), and you may assume that calls are being made to the system in chronological order (i.e., timestamp is monotonically increasing). Several hits may arrive roughly at the same time.
#
#  Implement the HitCounter class:
#
#
#  	HitCounter() Initializes the object of the hit counter system.
#  	void hit(int timestamp) Records a hit that happened at timestamp (in seconds). Several hits may happen at the same timestamp.
#  	int getHits(int timestamp) Returns the number of hits in the past 5 minutes from timestamp (i.e., the past 300 seconds).
#
#
#
#  Example 1:
#
#  Input
#  ["HitCounter", "hit", "hit", "hit", "getHits", "hit", "getHits", "getHits"]
#  [[], [1], [2], [3], [4], [300], [300], [301]]
#  Output
#  [null, null, null, null, 3, null, 4, 3]
#
#  Explanation
#  HitCounter hitCounter = new HitCounter();
#  hitCounter.hit(1);       // hit at timestamp 1.
#  hitCounter.hit(2);       // hit at timestamp 2.
#  hitCounter.hit(3);       // hit at timestamp 3.
#  hitCounter.getHits(4);   // get hits at timestamp 4, return 3.
#  hitCounter.hit(300);     // hit at timestamp 300.
#  hitCounter.getHits(300); // get hits at timestamp 300, return 4.
#  hitCounter.getHits(301); // get hits at timestamp 301, return 3.
#
#
#
#  Constraints:
#
#
#  	1 <= timestamp <= 2 * 10⁹
#  	All the calls are being made to the system in chronological order (i.e., timestamp is monotonically increasing).
#  	At most 300 calls will be made to hit and getHits.
#
#
#
#  Follow up: What if the number of hits per second could be huge? Does your design scale?

import unittest
from collections import deque


#  start_marker
class HitCounter:
    def __init__(self):
        self._hitq: deque[int] = deque()
        self._hctr = 0

    def hit(self, timestamp: int) -> None:
        self._hctr += 1
        self._hitq.append(timestamp)

    def getHits(self, timestamp: int) -> int:
        while self._hitq and timestamp - self._hitq[0] >= 300:
            self._hitq.popleft()
            self._hctr -= 1
        return self._hctr
        #  end_marker


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.hc = HitCounter()
        return super().setUp()

    def test_case_1(self):
        self.hc.hit(1)
        self.hc.hit(2)
        self.hc.hit(3)
        self.assertEqual(self.hc.getHits(4), 3)

    def test_case_2(self):
        self.hc.hit(1)
        self.assertEqual(self.hc.getHits(300), 1)
        self.assertEqual(self.hc.getHits(301), 0)


if __name__ == "__main__":
    unittest.main()
