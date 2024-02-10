#  Category: algorithms
#  Level: Medium
#  Percent: 56.811977%
# pylint: enable=useless-suppression
# pylint: disable=invalid-name, line-too-long, too-few-public-methods
# pylint: disable=missing-class-docstring, missing-function-docstring, missing-module-docstring


#  Given a list of accounts where each element accounts[i] is a list of
#  strings, where the first element accounts[i][0] is a name, and the rest of
#  the elements are emails representing emails of the account.
#
#  Now, we would like to merge these accounts. Two accounts definitely belong
#  to the same person if there is some common email to both accounts. Note that
#  even if two accounts have the same name, they may belong to different people
#  as people could have the same name. A person can have any number of accounts
#  initially, but all of their accounts definitely have the same name.
#
#  After merging the accounts, return the accounts in the following format: the
#  first element of each account is the name, and the rest of the elements are
#  emails in sorted order. The accounts themselves can be returned in any
#  order.
#
#
#  Example 1:
#
#  Input: accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
#  Output: [["John","john00@mail.com","john_newyork@mail.com","johnsmith@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
#  Explanation:
#  The first and second John's are the same person as they have the common email "johnsmith@mail.com".
#  The third John and Mary are different people as none of their email addresses are used by other accounts.
#  We could return these lists in any order, for example the answer [['Mary', 'mary@mail.com'], ['John', 'johnnybravo@mail.com'],
#  ['John', 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com']] would still be accepted.
#
#
#  Example 2:
#
#  Input: accounts = [["Gabe","Gabe0@m.co","Gabe3@m.co","Gabe1@m.co"],["Kevin","Kevin3@m.co","Kevin5@m.co","Kevin0@m.co"],["Ethan","Ethan5@m.co","Ethan4@m.co","Ethan0@m.co"],["Hanzo","Hanzo3@m.co","Hanzo1@m.co","Hanzo0@m.co"],["Fern","Fern5@m.co","Fern1@m.co","Fern0@m.co"]]
#  Output: [["Ethan","Ethan0@m.co","Ethan4@m.co","Ethan5@m.co"],["Gabe","Gabe0@m.co","Gabe1@m.co","Gabe3@m.co"],["Hanzo","Hanzo0@m.co","Hanzo1@m.co","Hanzo3@m.co"],["Kevin","Kevin0@m.co","Kevin3@m.co","Kevin5@m.co"],["Fern","Fern0@m.co","Fern1@m.co","Fern5@m.co"]]
#
#
#
#  Constraints:
#
#
#  	1 <= accounts.length <= 1000
#  	2 <= accounts[i].length <= 10
#  	1 <= accounts[i][j].length <= 30
#  	accounts[i][0] consists of English letters.
#  	accounts[i][j] (for j > 0) is a valid email.
#

import pickle
import unittest
from collections import defaultdict
from typing import Dict, List


#  start_marker
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        email_dict: Dict[str, int] = {}
        for i, acc in enumerate(accounts):
            k, *v = acc
            new_emails = set(v)
            for email in set(v):
                if email in email_dict and email_dict[email] != i:
                    old_idx = email_dict[email]
                    old_v = accounts[old_idx][1:]
                    new_emails |= set(old_v)
                    for e in old_v:
                        email_dict[e] = i
                    accounts[old_idx] = []
                email_dict[email] = i
            accounts[i] = [k] + sorted(list(new_emails))
        return list([x for x in accounts if x])
        # end_marker

    def accountsMerge_old_sad(self, accounts: List[List[str]]) -> List[List[str]]:
        email_dict: Dict[str, int] = {}
        end_marker = len(accounts)
        curr = 0
        while curr < end_marker:
            add_point = curr
            k, *v = accounts[curr]
            add_point_email_set = set(v)
            for email in add_point_email_set:
                if email in email_dict:
                    add_point = email_dict[email]
                    old_k, *old_v = accounts[add_point]
                    if old_k != k:
                        raise ValueError(f"old_k: {old_k}, k: {k}")
                    working_set = set(old_v) | set([email])
                    accounts[add_point] = [k] + list(working_set)
                    accounts[curr] = None
                email_dict[email] = add_point
            curr += 1
        return accounts

    def accountsMerge_old_but_works(self, accounts: List[List[str]]) -> List[List[str]]:
        merged_accounts: defaultdict[str, List] = defaultdict(list)
        email_dict: Dict[str, int] = {}
        for k, *v in accounts:
            new_acc = set(v)
            existing = merged_accounts[k]
            # print(f"does {new_acc} exist in {k}?")
            # if not existing:
            #     print(f"adding new account: {new_acc} to {k}: {existing}")
            # else:
            #     print(f"existing: {existing}")
            existing.append(new_acc)
            current = len(existing) - 1
            # print(f"email_dict: {email_dict}")
            # print(f"merged_accounts: {merged_accounts}")
            for email in new_acc:
                if email in email_dict:
                    # print(f"email {email} already exists")
                    old_index = email_dict[email]
                    if old_index != current:
                        # print(f"merging {old_index} to {current}")
                        # print(f"existing[old_index]: {existing[old_index]}")
                        merged = existing[current] | existing[old_index]
                        existing[current] = merged
                        for e in existing[old_index]:
                            email_dict[e] = current
                        existing[old_index] = None
                        # print(f"existing[current]: {existing[current]}")
                    # print(f"merged_accounts for {k}: {merged_accounts[k]}")
                else:
                    # print(f"email {email} does not exist")
                    email_dict[email] = current
            # print("----------------")
            # print(f"email_dict: {email_dict}")
            # print(f"merged_accounts: {merged_accounts}")
            # print("---------------------------------")
        retval = []
        for k, v in merged_accounts.items():
            for e in v:
                if e is not None:
                    retval.append([k] + sorted(list(e)))
        return retval


# for k, *v in accounts:
#     print(f"k: {k}, v: {v}")
#     merged_accounts[k].extend(v)
#     print(f"merged_accounts: {merged_accounts}")
# retval = []
# for k, v in merged_accounts.items():
#     retval.append([k] + list(set(v)))
# return retval


def set_equal(a: List[List[str]], b: List[List[str]]) -> bool:
    if len(a) != len(b):
        print(f"length not equal: {len(a)} != {len(b)}")
        print(f"a: {a}")
        print(f"b: {b}")
        return False
    a_dict = {k: set(v) for k, *v in a}
    b_dict = {k: set(v) for k, *v in b}
    for k, v in a_dict.items():
        if v != b_dict[k]:
            print(f"key {k} not equal")
            print(f"a: {v}")
            print(f"b: {b_dict[k]}")
            return False
    return True


#  end_marker
class TestSolution(unittest.TestCase):
    def test_case_1(self):
        accounts = [
            ["John", "johnsmith@mail.com", "john_newyork@mail.com"],
            ["John", "johnsmith@mail.com", "john00@mail.com"],
            ["Mary", "mary@mail.com"],
            ["John", "johnnybravo@mail.com"],
        ]
        result = Solution().accountsMerge(accounts)
        expected = [
            ["John", "john00@mail.com", "john_newyork@mail.com", "johnsmith@mail.com"],
            ["Mary", "mary@mail.com"],
            ["John", "johnnybravo@mail.com"],
        ]
        self.assertTrue(set_equal(result, expected))

    def test_case_2(self):
        accounts = [
            ["Gabe", "Gabe0@m.co", "Gabe3@m.co", "Gabe1@m.co"],
            ["Kevin", "Kevin3@m.co", "Kevin5@m.co", "Kevin0@m.co"],
            ["Ethan", "Ethan5@m.co", "Ethan4@m.co", "Ethan0@m.co"],
            ["Hanzo", "Hanzo3@m.co", "Hanzo1@m.co", "Hanzo0@m.co"],
            ["Fern", "Fern5@m.co", "Fern1@m.co", "Fern0@m.co"],
        ]
        expected = [
            ["Ethan", "Ethan0@m.co", "Ethan4@m.co", "Ethan5@m.co"],
            ["Gabe", "Gabe0@m.co", "Gabe1@m.co", "Gabe3@m.co"],
            ["Hanzo", "Hanzo0@m.co", "Hanzo1@m.co", "Hanzo3@m.co"],
            ["Kevin", "Kevin0@m.co", "Kevin3@m.co", "Kevin5@m.co"],
            ["Fern", "Fern0@m.co", "Fern1@m.co", "Fern5@m.co"],
        ]
        result = Solution().accountsMerge(accounts)
        self.assertTrue(set_equal(result, expected))

    def test_case_3(self):
        accounts = [
            ["David", "David0@m.co", "David4@m.co", "David3@m.co"],
            ["David", "David5@m.co", "David5@m.co", "David0@m.co"],
            ["David", "David1@m.co", "David4@m.co", "David0@m.co"],
            ["David", "David0@m.co", "David1@m.co", "David3@m.co"],
            ["David", "David4@m.co", "David1@m.co", "David3@m.co"],
        ]
        # [["David","David0@m.co","David3@m.co","David4@m.co","David5@m.co"],["David","David0@m.co","David1@m.co","David3@m.co","David4@m.co"],["David","David0@m.co","David1@m.co","David3@m.co","David4@m.co"],["David","David0@m.co","David1@m.co","David3@m.co","David4@m.co"]]
        expected = [
            [
                "David",
                "David0@m.co",
                "David1@m.co",
                "David3@m.co",
                "David4@m.co",
                "David5@m.co",
            ]
        ]
        result = Solution().accountsMerge(accounts)
        self.assertTrue(set_equal(result, expected))

    def test_case_4(self):
        with open("data/0721_TEST_4_ACC.dat", "rb") as f:
            accounts = pickle.load(f)
        result = Solution().accountsMerge(accounts)
        # print(result)
        # print(len(result))
        self.assertTrue(len(result) == 1)

    def test_case_5(self):
        accounts = [
            ["John", "johnsmith@mail.com", "john_newyork@mail.com"],
            ["John", "johnsmith@mail.com", "john00@mail.com"],
            ["Mary", "mary@mail.com"],
            ["John", "johnnybravo@mail.com"],
        ]
        expected = [
            ["John", "john00@mail.com", "john_newyork@mail.com", "johnsmith@mail.com"],
            ["Mary", "mary@mail.com"],
            ["John", "johnnybravo@mail.com"],
        ]
        result = Solution().accountsMerge(accounts)
        self.assertTrue(set_equal(result, expected))

    def test_case_6(self):
        accounts = [
            ["Gabe", "Gabe0@m.co", "Gabe3@m.co", "Gabe1@m.co"],
            ["Kevin", "Kevin3@m.co", "Kevin5@m.co", "Kevin0@m.co"],
            ["Ethan", "Ethan5@m.co", "Ethan4@m.co", "Ethan0@m.co"],
            ["Hanzo", "Hanzo3@m.co", "Hanzo1@m.co", "Hanzo0@m.co"],
            ["Fern", "Fern5@m.co", "Fern1@m.co", "Fern0@m.co"],
        ]
        expected = [
            ["Ethan", "Ethan0@m.co", "Ethan4@m.co", "Ethan5@m.co"],
            ["Gabe", "Gabe0@m.co", "Gabe1@m.co", "Gabe3@m.co"],
            ["Hanzo", "Hanzo0@m.co", "Hanzo1@m.co", "Hanzo3@m.co"],
            ["Kevin", "Kevin0@m.co", "Kevin3@m.co", "Kevin5@m.co"],
            ["Fern", "Fern0@m.co", "Fern1@m.co", "Fern5@m.co"],
        ]
        result = Solution().accountsMerge(accounts)
        self.assertTrue(set_equal(result, expected))


if __name__ == "__main__":
    unittest.main()

    # accounts = [
    #     ["David", "David0@m.co", "David4@m.co", "David3@m.co"],
    #     ["David", "David5@m.co", "David5@m.co", "David0@m.co"],
    #     ["David", "David1@m.co", "David4@m.co", "David0@m.co"],
    #     ["David", "David0@m.co", "David1@m.co", "David3@m.co"],
    #     ["David", "David4@m.co", "David1@m.co", "David3@m.co"],
    # ]
    # # [["David","David0@m.co","David3@m.co","David4@m.co","David5@m.co"],["David","David0@m.co","David1@m.co","David3@m.co","David4@m.co"],["David","David0@m.co","David1@m.co","David3@m.co","David4@m.co"],["David","David0@m.co","David1@m.co","David3@m.co","David4@m.co"]]
    # expected = [
    #     [
    #         "David",
    #         "David0@m.co",
    #         "David1@m.co",
    #         "David3@m.co",
    #         "David4@m.co",
    #         "David5@m.co",
    #     ]
    # ]
    # result = Solution().accountsMerge(accounts)
    # print(len(result))
    # print(result)
    #
    # print(set_equal(expected, result))
    # accounts = [
    #     ["John", "johnsmith@mail.com", "john_newyork@mail.com"],
    #     ["John", "johnsmith@mail.com", "john00@mail.com"],
    #     ["Mary", "mary@mail.com"],
    #     ["John", "johnnybravo@mail.com"],
    # ]
    # result = Solution().accountsMerge(accounts)
    # print(result)
    # print(len(result))
