from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i1,n1 in enumerate(numbers):
            for i2,n2 in enumerate(numbers[i1+1:]):
                if n1 + n2 == target:
                    return [i1+1, i1+i2+1+1]