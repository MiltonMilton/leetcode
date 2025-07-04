from collections import defaultdict
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_count = defaultdict(int)
        for num in nums:
            nums_count[num] += 1
        sorted_items = sorted(nums_count.items(), key=lambda x: x[1], reverse=True)
        sorted_dict = dict(sorted_items)
        return list(sorted_dict.keys())[:k]



if __name__ == '__main__':
    solution = Solution()
    output = solution.topKFrequent([1,2,2,3,4,5,6,7], 2)
    print(output)

