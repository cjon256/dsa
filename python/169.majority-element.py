from collections import Counter


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ctr = Counter(nums)
        return ctr.most_common(1)[0][0]
