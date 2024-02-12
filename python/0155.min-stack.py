#  Category: algorithms
#  Level: Medium
#  Percent: 53.688847%
# pylint: enable=useless-suppression
# pylint: disable=invalid-name, line-too-long, too-few-public-methods
# pylint: disable=missing-class-docstring, missing-function-docstring, missing-module-docstring


#  Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
#
#  Implement the MinStack class:
#
#
#  	MinStack() initializes the stack object.
#  	void push(int val) pushes the element val onto the stack.
#  	void pop() removes the element on the top of the stack.
#  	int top() gets the top element of the stack.
#  	int getMin() retrieves the minimum element in the stack.
#
#
#  You must implement a solution with O(1) time complexity for each function.
#
#
#  Example 1:
#
#  Input
#  ["MinStack","push","push","push","getMin","pop","top","getMin"]
#  [[],[-2],[0],[-3],[],[],[],[]]
#
#  Output
#  [null,null,null,null,-3,null,0,-2]
#
#  Explanation
#  MinStack minStack = new MinStack();
#  minStack.push(-2);
#  minStack.push(0);
#  minStack.push(-3);
#  minStack.getMin(); // return -3
#  minStack.pop();
#  minStack.top();    // return 0
#  minStack.getMin(); // return -2
#
#
#
#  Constraints:
#
#
#  	-2³¹ <= val <= 2³¹ - 1
#  	Methods pop, top and getMin operations will always be called on non-empty stacks.
#  	At most 3 * 10⁴ calls will be made to push, pop, top, and getMin.
#


import unittest


#  start_marker
class MinStack:

    def __init__(self):
        self._stack = []
        self._min = []

    def push(self, val: int) -> None:
        self._stack.append(val)
        if len(self._min) == 0:
            self._min.append(val)
        else:
            self._min.append(min(val, self._min[-1]))

    def pop(self) -> None:
        if len(self._stack) == 0:
            return
        del self._stack[-1]
        del self._min[-1]

    def top(self) -> int:
        return self._stack[-1]

    def getMin(self) -> int:
        return self._min[-1]

    #  end_marker
    def dummy(self):
        pass


class MinStack_plus_alpha:
    # from https://leetcode.com/problems/min-stack/solutions/3775651/python-99-95-faster-only-one-stack

    def __init__(self):
        self.st = []  # stack
        self.min = 0  # min value
        print(f"self.st: {self.st}, self.min: {self.min}")

    def push(self, val: int) -> None:
        print(f"push: {val}")
        if len(self.st) == 0:
            self.st.append(val)
            self.min = val
        else:
            if val >= self.min:
                self.st.append(val)
            else:
                self.st.append(2 * val - self.min)
                self.min = val
        print(f"self.st: {self.st}, self.min: {self.min}")

    def pop(self) -> None:
        print(f"pop {self.st[-1]}")
        x = self.st.pop()
        if x < self.min:
            self.min = 2 * self.min - x
        print(f"self.st: {self.st}, self.min: {self.min}")

    def top(self) -> int:
        print(f"top {self.st[-1]}")
        print(f"self.st: {self.st}, self.min: {self.min}")
        x = self.st[-1]
        if x >= self.min:
            return x
        return self.min

    def getMin(self) -> int:
        print("getMin")
        print(f"self.st: {self.st}, self.min: {self.min}")
        return self.min


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
class TestSolution(unittest.TestCase):
    def test_case_1(self):
        min = MinStack()
        min.push(-2)
        min.push(0)
        min.push(-3)
        self.assertEqual(min.getMin(), -3)
        min.pop()  # oddly, does not return a value
        self.assertEqual(min.top(), 0)
        self.assertEqual(min.getMin(), -2)


if __name__ == "__main__":
    # unittest.main()
    min2 = MinStack_plus_alpha()
    min2.push(-2)
    min2.push(0)
    min2.push(-3)
    print(min2.getMin())
    min2.pop()
    print(min2.top())
    print(min2.getMin())
    min2.pop()
    min2.pop()
    print(min2.getMin())
    min2.push(3)
    min2.push(2)
    min2.push(1)
    min2.push(1)
    min2.push(1)
    min2.push(0)
    min2.push(-8)
    min2.push(-9)
    min2.pop()
    min2.pop()
    min2.pop()
    min2.pop()
    min2.pop()
    min2.pop()
    min2.pop()
    min2.pop()
    min2.push(1001)
