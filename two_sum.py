from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for primary_index, primary_number in enumerate(nums):
            for secondary_index, secondary_number in enumerate(nums[primary_index + 1:]):
                if primary_number + secondary_number == target:
                    return [primary_index, 1 + primary_index + secondary_index]
