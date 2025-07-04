from typing import List


class Solution:
    # def productExceptSelf(self, nums: List[int]) -> List[int]:
    #     output = []
    #     for index, _ in enumerate(nums):
    #         output.append(math.prod(nums[:index] + nums[index+1:]))
    #     return output

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        output = [1] * n

        for i in range(1,n):
           output[i] = output[i-1] * nums[i-1]

        prod = nums[n-1]
        for i in range(n-2, -1, -1):
            output[i] = output[i] * prod
            prod = prod * nums[i]

        return output


if __name__ == "__main__":
    s = Solution()
    print(s.productExceptSelf([1,2,4,6]))
