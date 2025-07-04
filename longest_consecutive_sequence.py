import heapq
import math
from collections import defaultdict
from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for num in numSet:
            if (num - 1) not in numSet:
                length = 1
                while (num + length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest

if __name__ == "__main__":
    s = Solution()
    print(s.longestConsecutive([0])) #1
    # print(s.longestConsecutive([0,3,2,5,4,6,1,1])) #7
    # print(s.longestConsecutive([2,20,4,10,3,4,5])) #4





