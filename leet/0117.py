import unittest
from dataclasses import dataclass
from pprint import pprint as pp
from typing import List, Optional, Tuple


@dataclass
class Node:
    val: int
    left: "Node" = None
    right: "Node" = None
    next: "Node" = None


@dataclass
class NextHolder:
    next: "Node" = None


class Solution:
    def connect(self, root: "Node") -> "Node":
        if root is None:
            return None
        completed_level_head = root
        working_level_head_holder = NextHolder()
        while completed_level_head is not None:
            completed_level_curr = completed_level_head
            working_level_tail = working_level_head_holder
            while completed_level_curr is not None:
                if completed_level_curr.left is not None:
                    working_level_tail.next = completed_level_curr.left
                    working_level_tail = working_level_tail.next
                if completed_level_curr.right is not None:
                    working_level_tail.next = completed_level_curr.right
                    working_level_tail = working_level_tail.next
                completed_level_curr = completed_level_curr.next
            completed_level_head = working_level_head_holder.next
            working_level_head_holder.next = None
        return root

    def connect_s(self, root: "Node") -> "Node":
        def max_depth(node: Node) -> int:
            if node is None:
                return 0
            return 1 + max(max_depth(node.left), max_depth(node.right))

        def nodes_at_depth_gen(node: Node, d: int) -> Optional[Node]:
            if node is None:
                return None
            if d == 0:
                yield node
            yield from nodes_at_depth_gen(node.left, d - 1)
            yield from nodes_at_depth_gen(node.right, d - 1)

        if root is None:
            return None
        d = max_depth(root)
        for i in range(d):
            nodes = nodes_at_depth_gen(root, i)
            prev_node = next(nodes)
            for node in nodes:
                prev_node.next = node
                prev_node = node
        return root

    def connect_nah(self, root: "Node") -> "Node":
        if not root:
            return None

        curr = root
        dummy = Node(-999)
        head = root

        while head:
            curr = head  # initialize current level's head
            prev = dummy  # init prev for next level linked list traversal
            # iterate through the linked-list of the current level and connect all the siblings in the next level
            print(f"curr: {curr.val if curr else None}, prev: {prev.val}")
            print(
                f"head: {head.val if head else None}, dummy.next: {dummy.next.val if dummy.next else None}"
            )
            print("=" * 20)
            while curr:
                print(f"curr: {curr.val if curr else None}, prev: {prev.val}")
                print(
                    f"head: {head.val if head else None}, dummy.next: {dummy.next.val if dummy.next else None}"
                )
                print("-" * 10)
                if curr.left:
                    print(f"curr.left: {curr.left.val}")
                    prev.next = curr.left
                    prev = prev.next
                if curr.right:
                    print(f"curr.right: {curr.right.val}")
                    prev.next = curr.right
                    prev = prev.next
                curr = curr.next
                print("-" * 20)
                print(f"curr: {curr.val if curr else None}, prev: {prev.val}")
                print(
                    f"head: {head.val if head else None}, dummy.next: {dummy.next.val if dummy.next else None}"
                )
                print("-" * 40)
            print("=" * 20)
            head = dummy.next  # update head to the linked list of next level
            dummy.next = None  # reset dummy node
            print(f"curr: {curr.val if curr else None}, prev: {prev.val}")
            print(
                f"head: {head.val if head else None}, dummy.next: {dummy.next.val if dummy.next else None}"
            )
            print("=" * 20)
            print("=" * 20)
        return root

    def connect_lo(self, root: "Node") -> "Node":
        def level_order_generator(top: Node) -> Tuple[int, Node]:
            if top is None:
                return
            queue = [(0, top)]
            while len(queue) > 0:
                clvl, node = queue.pop(0)
                yield clvl, node
                if node.left is not None:
                    queue.append((clvl + 1, node.left))
                if node.right is not None:
                    queue.append((clvl + 1, node.right))

        if root is None:
            return None
        level_order = level_order_generator(root)
        prev_lvl, prev_node = next(level_order)
        for lvl, node in level_order:
            if prev_lvl == lvl:
                prev_node.next = node
            else:
                prev_lvl = lvl
            prev_node = node
        return root

    def inorder(self, root: Node) -> None:
        if root is None:
            return
        self.inorder(root.left)
        self.inorder(root.right)
        print(root.val)


# convert array to tree
def array_to_tree(array: List[int]) -> List[Node]:
    tree_array = [None] * len(array)
    for i in range(len(array)):
        if array[i] is not None:
            tree_array[i] = Node(array[i])
    for i in range(len(array)):
        if tree_array[i] is not None:
            left_index = 2 * i + 1
            right_index = 2 * i + 2
            if left_index < len(array):
                tree_array[i].left = tree_array[left_index]
            if right_index < len(array):
                tree_array[i].right = tree_array[right_index]
    return tree_array


def pretty_print(root: Node) -> None:
    def _pretty_print(root: Node, level: int) -> None:
        if root is None:
            return
        _pretty_print(root.right, level + 1)
        print(
            " " * 4 * level + "->", root.val, ":", root.next.val if root.next else None
        )
        _pretty_print(root.left, level + 1)

    _pretty_print(root, 0)


class TestSolution(unittest.TestCase):
    def test_connect_1(self):
        nodes = array_to_tree([0, 1, 2, 3, 4, 5, 6, 7])
        root = nodes[0]
        Solution().connect(root)
        assert root.next is None
        assert nodes[1].next == nodes[2]
        assert nodes[2].next is None
        assert nodes[3].next == nodes[4]
        assert nodes[4].next == nodes[5]
        assert nodes[5].next == nodes[6]
        assert nodes[6].next is None
        assert nodes[7].next is None

    def test_connect_2(self):
        nodes = array_to_tree([0, 1, 2, 3, 4, 5, 6, 7, 8])
        root = nodes[0]
        Solution().connect(root)
        assert nodes[0].next is None
        assert nodes[1].next == nodes[2]
        assert nodes[2].next is None
        assert nodes[3].next == nodes[4]
        assert nodes[4].next == nodes[5]
        assert nodes[5].next == nodes[6]
        assert nodes[6].next is None
        assert nodes[7].next is nodes[8]
        assert nodes[8].next is None

    def test_connect_3(self):
        nodes = array_to_tree([0, 1, 2, None, 4, None, 6])
        root = nodes[0]
        Solution().connect(root)
        assert nodes[0].next is None
        assert nodes[1].next is nodes[2]
        assert nodes[2].next is None
        assert nodes[4].next is nodes[6]
        assert nodes[6].next is None

    def test_connect_4(self):
        nodes = array_to_tree([0, 1, 2, 3, None, None, 6])
        root = nodes[0]
        Solution().connect(root)
        assert nodes[0].next is None
        assert nodes[1].next is nodes[2]
        assert nodes[2].next is None
        assert nodes[3].next is nodes[6]
        assert nodes[6].next is None


if __name__ == "__main__":
    unittest.main()
    # result = Solution().connect(array_to_tree([0, 1, 2, 3, None, None, 6])[0])
    # pretty_print(result)
